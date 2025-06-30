# ========================================================================================
# parser.py
#
# FILE OVERVIEW:
# This module is responsible for the "P" in ETL (Extract, Transform, Load).
# Its primary job is to take a URL or raw web content and parse it. It turns
# unstructured or semi-structured web data (like XML) into a format that Python
# can easily understand and work with (like a list of BeautifulSoup objects).
# ========================================================================================

# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from error_log import setup_logger
import config

# Setup logger for debugging
logger = setup_logger(__name__)

# This is your original function, it fetches a live URL and parses it.
def get_rss_items_from_url(url):
    """
    Fetches and parses a LIVE RSS feed from a given URL.
    This function is used for non-historical scraping. It performs two actions:
    1. Makes an HTTP request to download the content from the URL.
    2. Passes the downloaded content to the dedicated parsing function.
    """
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
    """
    Parses XML content that has ALREADY been downloaded.
    This function is a reusable tool. It doesn't download anything itself, making it
    perfect for the historical module, which downloads the content separately.
    """
    try:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        items = soup.find_all("item")
    
        if not items:
            logger.warning(f"No <item> tags found in content from {source_url}")
    
        return items
    except Exception as e:
        logger.error(f"Failed to parse XML content from {source_url}: {e}")
        return []