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

    # Create combined text for NLP analysis
    text_for_analysis = f"{title}. {description_clean}"

    # Define our candidate categories for the model to choose from.
    candidate_categories = config.candidate_categories
    detected_category = pre_defined_category if pre_defined_category else spacy_detect.detect_category_zero_shot(text_for_analysis, candidate_categories)
    detected_country = pre_defined_country if pre_defined_country else spacy_detect.detect_country_ner(text_for_analysis)

    raw_date = item.find("pubDate").text.strip() if item.find("pubDate") else ""
    normalized_date = normalize_date_format(raw_date)
    
    # Assemble the final, clean dictionary for this article.
    filtered_item = {
        "title": title,
        "description": description_clean,
        "date": normalized_date,
        "url": item.find("link").text.strip() if item.find("link") else "",
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
