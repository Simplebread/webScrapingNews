# ========================================================================================
# filter.py
#
# FILE OVERVIEW:
# This module is the "brain" of the data processing pipeline. Its main responsibility
# is to take the raw, parsed data (a list of article objects), and then clean,
# enrich, and structure it. It extracts key information like title and description,
# removes unwanted HTML, and intelligently assigns a country and category based on
# keywords defined in the config file. It also handles the initial de-duplication
# of articles before they are sent to the database.
# ========================================================================================

# Import necessary libraries
import config
import parser as parser
from bs4 import BeautifulSoup
from error_log import setup_logger
import historical
import spacy_detect
from dateutil.parser import parse as parse_date
import re

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running filter on new RSS feed and Wayback Machine snapshots.")

# Filter using keywords
def filtered_list(url, source, pre_defined_country, pre_defined_category, is_historical=False, start_date=None, end_date=None):
    """
    Acts as the main controller for processing a single feed URL.
    It decides whether to call the historical module or the live parser,
    then sends the results to be processed item by item.
    """
    logger.debug(f"Fetching: {url}")

    filtered_data = []

    # --- Logic Branch: Historical vs. Live ---
    if is_historical:
        # Get historical URLs and filter them by date range
        logger.info("Fetching historical documents...")
        historical_items = historical.fetch_historical_documents(url, start_date, end_date)
        
        # Process the historical items
        for item in historical_items:
            filtered_data.extend(process_item(item, source, pre_defined_country, pre_defined_category))
    else:
        # Regular RSS Feed processing
        items = parser.get_rss_items_from_url(url)
        
        # --- Item Processing ---
        # Loop through each article <item> that was found.
        for item in items:
            filtered_data.extend(process_item(item, source, pre_defined_country, pre_defined_category))

    # Debugging
    logger.info(f"Filtered {len(filtered_data)} items from {url}")
    return filtered_data

# Function to process individual items (RSS or historical)
def process_item(item, source, pre_defined_country, pre_defined_category):
    """
    Takes a single raw article <item> and transforms it into a clean,
    structured dictionary using NLP for detection.
    """
    title_tag = item.find("title")
    title = title_tag.text.strip() if title_tag else ""

    desc_tag = item.find("description")
    description_raw = desc_tag.text.strip() if desc_tag else ""

    soup = BeautifulSoup(description_raw, "html.parser")
    description_clean = soup.get_text(separator=" ", strip=True)

    url = item.find("link").text.strip() if item.find("link") else ""

    # Create combined text for NLP analysis
    text_for_analysis = f"{title}. {description_clean}"

    lang = spacy_detect.detect_lang(text_for_analysis)
    if lang!= "en":
        text_for_analysis = spacy_detect.ensure_english(text_for_analysis)
    else:
        text_for_analysis = text_for_analysis

    # Fallback system using keywords
    detected_country = pre_defined_country
    if not detected_country:
        detected_country = spacy_detect.detect_country_ner(text_for_analysis)

        # 3. If the NLP model returns "Unknown", THEN fall back to our keyword search.
        if detected_country == "Unknown":
            logger.debug(f"NLP country detection failed for '{title[:30]}...'. Falling back to keyword search.")
            detected_country = detect_country_keywords(text_for_analysis)

    # --- Category Detection (can also use a fallback if desired) ---
    detected_category = pre_defined_category
    if not detected_category:
        # Assumes you have a list named 'candidate_categories' in your config.py
        candidate_categories = config.candidate_categories
        detected_category = spacy_detect.detect_category_zero_shot(text_for_analysis, candidate_categories)

        if detected_category == "General":
            logger.debug(f"NLP category detection failed for '{title[:30]}...'. Falling back to keyword search.")
            detected_category = detect_category_keywords(text_for_analysis)
        # You could add a keyword fallback for category here as well if needed.

    if item.find("pubDate"):
        raw_date = item.find("pubDate").text.strip()
    elif item.find("dc:date"):
        raw_date = item.find("dc:date").text.strip()
    else:
        raw_date = ""

    normalized_date = normalize_date_format(raw_date)
    
    # Assemble the final, clean dictionary for this article.
    filtered_item = {
        "title": title,
        "description": description_clean,
        "date": normalized_date,
        "url": url,
        "source": source,
        "country": detected_country,
        "category": detected_category
    }
    return [filtered_item]

def detect_duplicate(items_list):
    """
    Removes duplicate articles from a list based on the article title.
    This version uses a Python 'set' for highly efficient lookups, which avoids
    the bugs and performance issues of a nested while loop.
    """
    seen_titles = set()
    unique_items = []

    # Loop through each article dictionary in the list.
    for item in items_list:
        # Check if the item is a dictionary and has a 'title' key to prevent errors.
        if isinstance(item, dict) and "title" in item:
            # Normalize the title for a consistent comparison (lowercase, no extra spaces).
            normalized_title = item["title"].strip().lower()
            
            # If we have NOT seen this title before, it's a unique article.
            if normalized_title not in seen_titles:
                # Add the title to our set of seen titles.
                seen_titles.add(normalized_title)
                # Add the unique article dictionary to our new list.
                unique_items.append(item)
        else:
            # This warning is the key to identifying bad data in the list.
            logger.warning(f"Skipping an invalid item during de-duplication: {item}")
            
    duplicates_removed = len(items_list) - len(unique_items)
    if duplicates_removed > 0:
        logger.info(f"Removed {duplicates_removed} duplicate articles found across all feeds.")

    return unique_items

def normalize_date_format(date_string):
    """
    Parses a date string in almost any format and returns it as 'YYYY-MM-DD'.
    """
    if not date_string:
        return ""
    try:
        # Use dateutil.parser to intelligently parse the date string.
        dt_object = parse_date(date_string)
        # Format the datetime object into a consistent string format.
        return dt_object.strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        # If the date string is un-parseable, log a warning and return it as is.
        logger.warning(f"Could not parse date: '{date_string}'. Leaving as is.")
        return date_string

def detect_country_keywords(text):
    """
    This is the original keyword-based country detection, now used as a fallback.
    """
    content = f"{text}".lower()
    for country, keywords in config.key_word_country.items():
        if any(keyword.lower() in content for keyword in keywords):
            logger.debug(f"Keyword fallback found country: '{country}'")
            return country
    return "Unknown"

def detect_category_keywords(text):
    """
    Safer fallback: Uses strict keyword matching with word boundaries.
    Prevents false positives like 'tech' in 'protection'.
    """
    content = f"{text}".lower()
    
    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            # Match only whole words or exact keyword phrases
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            if re.search(pattern, content):
                logger.debug(f"Keyword fallback hit on keyword '{keyword}' for category '{category}'")
                return category
    
    return "General"