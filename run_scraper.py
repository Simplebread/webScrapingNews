# Import necessary libraries
import pandas as pd
import config as config
import parser as parser

# Create Variable
all_news = []

# Practice Output
for feed in config.rss_feeds:
    results = parser.filter_list(feed["url"],feed["country"],feed["source"])
    all_news.extend(results)

# Create data frame for CSV
df = pd.DataFrame(all_news)
df.to_csv("news.csv", index=False, encoding='utf-8')