# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Create data list
newsData = []

# Create a variable to store RSS news link
linkBBC = requests.get("https://feeds.bbci.co.uk/news/rss.xml").text

# Create soup and parse using lxml
soup = BeautifulSoup(linkBBC, "lxml-xml")

# Filter and Sort
items = soup.find_all("item")

# Output items
for item in items:
    newsData.append({
        "title": item.title.text,
        "date": item.pubDate.text,
        "description": item.description.text,
        "url": item.link.text
    })

# Convert data frame into csv
df = pd.DataFrame(newsData)
df.to_csv("bbc_news.csv", index=False, encoding='utf-8')