# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Create function for parsing RSS
def get_rss_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml-xml")
    return soup.find_all("item")