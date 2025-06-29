# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from error_log import setup_logger
import config

# Setup logger for debugging
logger = setup_logger(__name__)

# This is your original function, it fetches a live URL and parses it.
def get_rss_items_from_url(url):
    logger.info(f"Fetching live RSS feed from: {url}")
    headers = config.user_agent

    # Request to rss links
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to retrieve request for {url}: {e}")
        return []

    # This calls our new parsing function to avoid duplicating code
    return parse_rss_content(response.content, source_url=url)


# This function takes content that is already downloaded and parses it.
def parse_rss_content(xml_content, source_url=""):
    try:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        items = soup.find_all("item")
    
        if not items:
            logger.warning(f"No <item> tags found in content from {source_url}")
    
        return items
    except Exception as e:
        logger.error(f"Failed to parse XML content from {source_url}: {e}")
        return []