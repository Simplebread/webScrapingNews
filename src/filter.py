# Import necessary libraries
import config as config
import parser as parser
from bs4 import BeautifulSoup
from error_log import setup_logger

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running filter on new RSS feed.")

# Filter using keywords
def filtered_list(url, source, country, category):

    # Debugging
    logger.debug(f"Fetching: {url}")

    # Create necesary variables 
    items = parser.get_rss_items(url)
    filtered_data = []

    # Fetch data from the title tag
    for item in items:
        title_tag = item.find("title")
        title = title_tag.text.strip() if title_tag else ""
        if not title:
            # Debugging
            logger.warning("Title not found in RSS item.")

        desc_tag = item.find("description")
        description = desc_tag.text.strip() if desc_tag else ""
        if not description:
            # Debugging
            logger.warning("Description not found in RSS item.") 

        # Parse again to get rid of complicated ugly news RSS inside description
        soup = BeautifulSoup(description, "html.parser")
        for tag in soup(["img", "style", "script"]):
            tag.decompose()
        description = soup.get_text(separator=" ", strip=True)

        # Detect country and category dynamically
        detected_country = country if country else detect_country(title, description)
        detected_category = category if category else detect_category(title, description)

        # Debugging
        logger.debug(f"Detected Country: {detected_country}, Category: {detected_category}")

        # Append all the data into the local variable which will be returned
        filtered_data.append({
            "title": title,
            "description": description,
            "date": item.find("pubDate").text if item.find("pubDate") else "",
            "url": item.find("link").text if item.find("link") else "",
            "source": source,
            "country": detected_country,
            "category": detected_category
        })
        
    # Debugging
    logger.info(f"Filtered {len(filtered_data)} items from {url}")
    return filtered_data

# Function to detect country
def detect_country(title, description):
    content = f"{title} {description}".lower()
    # Check the values of the keys and comparing them for keywords
    for country, keywords in config.key_word_country.items():
        for keyword in keywords:
            if keyword.lower() in content:
                logger.debug(f"Found keyword '{keyword}' for country '{country}'")
                return country
    logger.warning("No country detected; defaulting to 'Unknown'")
    return "Unknown"


# Functino to detect category
def detect_category(title, description):
    content = f"{title} {description}".lower()
    # Check the values of the keys and comparing them for keywords
    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            if keyword.lower() in content:
                logger.debug(f"Found keyword '{keyword}' for category '{category}'")
                return category
    logger.warning("No category detected; defaulting to 'General'")
    return "General"


# Function to detect duplicate in news and article entries
def detect_duplicate(list):
    # Nested loop to go through the whole list
    new_list = list
    i = 0
    while i<len(new_list):
        j = i + 1
        while j<len(new_list):
            # Compares one title to everything in the list
            if new_list[i]["title"].strip().lower() == new_list[j]["title"].strip().lower():
                new_list.pop(j)
            else:
                j+=1
        i+=1
    return new_list
