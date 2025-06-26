# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from error_log import setup_logger

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running parser to get request URLs.")

# Create function for parsing RSS
def get_rss_items(url):
    # header to deal with HTTPS issue
    headers = {"User-Agent": "Mozilla/5.0"}

    # get the xml from the RSS link
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except:
        # Debugging
        logger.error(f"Fail to retrieve request for {url}")

    # Parses the information and transforms it into text for readability
    soup = BeautifulSoup(response.text, "lxml-xml")
    return soup.find_all("item")
