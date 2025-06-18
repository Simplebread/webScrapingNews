# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Create function for parsing RSS
def get_rss_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml-xml")
    return soup.find_all("item")

# # Import necessary libraries
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import config as config

# # Output items
# def filter_list(url, country, source):
#     # Create local variable
#     news_data = []
#     # Request the RSS link
#     request_link = requests.get(url).text
#     # Create soup and parse using lxml
#     soup = BeautifulSoup(request_link, "lxml-xml")
#     # Filter and Sort
#     items = soup.find_all("item")

#     # Append items to the list
#     for item in items:
#         news_data.append({
#             "title": item.find("title").text if item.find("title") else "",
#             "date": item.find("pubDate").text if item.find("pubDate") else "",
#             "source": source,
#             "country": country,
#             "description": item.find("description").text if item.find("description") else "",
#             "url": item.find("link").text if item.find("link") else ""
#         })
#     return news_data

