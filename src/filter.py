# Import necessary libraries
import config as config
import parser as parser
from bs4 import BeautifulSoup
from error_log import setup_logger
import historical

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running filter on new RSS feed and Wayback Machine snapshots.")

# Filter using keywords
def filtered_list(url, source, country, category, is_historical=False, start_date=None, end_date=None):
    logger.debug(f"Fetching: {url}")

    filtered_data = []

    if is_historical:
        # Get historical URLs and filter them by date range
        logger.info("Fetching historical documents...")
        historical_items = historical.fetch_historical_documents(url, start_date, end_date)
        
        # Process the historical items
        for item in historical_items:
            filtered_data.extend(process_item(item, source, country, category))
    else:
        # Regular RSS Feed processing
        items = parser.get_rss_items(url)
        
        # Process the RSS items
        for item in items:
            filtered_data.extend(process_item(item, source, country, category))

    # Debugging
    logger.info(f"Filtered {len(filtered_data)} items from {url}")
    return filtered_data

# Function to process individual items (RSS or historical)
def process_item(item, source, country, category):
    filtered_item = {}

    # Extract title and description
    title_tag = item.find("title")
    title = title_tag.text.strip() if title_tag else ""
    if not title:
        logger.warning("Title not found in item.")

    desc_tag = item.find("description")
    description = desc_tag.text.strip() if desc_tag else ""
    if not description:
        logger.warning("Description not found in item.") 

    # Parse again to get rid of complicated ugly news RSS inside description
    soup = BeautifulSoup(description, "html.parser")
    for tag in soup(["img", "style", "script"]):
        tag.decompose()
    description = soup.get_text(separator=" ", strip=True)

    # Detect country and category dynamically
    detected_country = country if country else detect_country(title, description)
    detected_category = category if category else detect_category(title, description)

    logger.debug(f"Detected Country: {detected_country}, Category: {detected_category}")

    # Build the filtered item
    filtered_item = {
        "title": title,
        "description": description,
        "date": item.find("pubDate").text if item.find("pubDate") else "",
        "url": item.find("link").text if item.find("link") else "",
        "source": source,
        "country": detected_country,
        "category": detected_category
    }

    # Ensure that filtered_item is appended
    logger.debug(f"Appending item: {filtered_item['title']}")
    return [filtered_item]

# Function to detect country
def detect_country(title, description):
    content = f"{title} {description}".lower()
    for country, keywords in config.key_word_country.items():
        for keyword in keywords:
            if keyword.lower() in content:
                logger.debug(f"Found keyword '{keyword}' for country '{country}'")
                return country
    logger.warning("No country detected; defaulting to 'Unknown'")
    return "Unknown"

# Function to detect category
def detect_category(title, description):
    content = f"{title} {description}".lower()
    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            if keyword.lower() in content:
                logger.debug(f"Found keyword '{keyword}' for category '{category}'")
                return category
    logger.warning("No category detected; defaulting to 'General'")
    return "General"

# Function to detect duplicates in news and article entries
def detect_duplicate(list):
    new_list = list
    i = 0
    while i < len(new_list):
        j = i + 1
        while j < len(new_list):
            if new_list[i]["title"].strip().lower() == new_list[j]["title"].strip().lower():
                new_list.pop(j)
            else:
                j += 1
        i += 1
    return new_list
