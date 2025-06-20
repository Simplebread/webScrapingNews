# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Create function for parsing RSS
def get_rss_items(url):
    # header to deal with HTTPS issue
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # raise exception if HTTP error
    except:
        "Fail to retrieve request"
    soup = BeautifulSoup(response.text, "lxml-xml")
    return soup.find_all("item")
