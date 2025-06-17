# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import rss_feeds as rf

# Create data list
news_data = []

# Output items
def filter_list(url, country, source):
        # Request the RSS link
        request_link = requests.get(url).text
        # Create soup and parse using lxml
        soup = BeautifulSoup(request_link, "lxml-xml")
        # Filter and Sort
        items = soup.find_all("item")

        # Append items to the list
        for item in items:
            news_data.append({
                "title": item.find("title").text if item.find("title") else "",
                "date": item.find("pubDate").text if item.find("pubDate") else "",
                "source": source,
                "country": country,
                "description": item.find("description").text if item.find("description") else "",
                "url": item.find("link").text if item.find("link") else ""
            })

# Practice Output
for feed in rf.rss_feeds:
    filter_list(feed["url"],feed["country"],feed["source"])

# Create data frame for CSV
df = pd.DataFrame(news_data)
df.to_csv("news.csv", index=False, encoding='utf-8')