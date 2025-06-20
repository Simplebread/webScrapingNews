# Import necessary libraries
import pandas as pd
import config as config
import parser as parser
import filter as filter

# Create Variable
all_news = []

# Practice Output
for feed in config.rss_feeds:
    try:
        results = filter.filtered_list(feed["url"], feed["source"], feed["country"], feed["category"])
        all_news.extend(results)
    except:
        print(f"[ERROR] Skipping {feed['url']}")

# Create data frame for CSV
df = pd.DataFrame(all_news)
df.to_csv("news.csv", index=False, encoding='utf-8')
