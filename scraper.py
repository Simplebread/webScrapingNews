# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Create a variable to store RSS news link
linkBBC = requests.get("https://feeds.bbci.co.uk/news/rss.xml").text

# Create soup and parse using lxml
soup = BeautifulSoup(linkBBC, "lxml-xml")

# Filter and Sort
titles = soup.find_all("title")
descriptions = soup.find_all("description")

for title, description in zip(titles[2:], descriptions[1:]):
    print(f"Title: {title.text}")
    print(f"Description: {description.text}\n")