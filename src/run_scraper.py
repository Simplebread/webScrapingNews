# Import necessary libraries
import config as config
import filter as filter
import data_base as db
from error_log import setup_logger

# Setup logger for debugging
logger = setup_logger(__name__)

# Create Variable
all_news = []

# Store results into variable
for feed in config.rss_feeds:
    try:
        # Inputs data from config.py to be processed
        results = filter.filtered_list(feed["url"], feed["source"], feed["country"], feed["category"])
        all_news.extend(results)
    except:
        # Debugging
        logger.error(f"Skipping {feed['url']}")

# Delete duplicate entries
all_news = filter.detect_duplicate(all_news)

# Create data base using SQL Lite
db.upload_data_base(all_news)
