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
        # If you want to scrape historical data, set is_historical=True and provide date range
        is_historical = True
        start_date = "2024-06-01"
        end_date = "2024-06-10"
        
        # Inputs data from config.py to be processed
        results = filter.filtered_list(
            feed["url"], 
            feed["source"], 
            feed["country"], 
            feed["category"], 
            is_historical=is_historical,
            start_date=start_date,
            end_date=end_date
        )
        all_news.extend(results)
    except Exception as e:
        # Debugging
        logger.error(f"Skipping {feed['url']} due to {str(e)}")

# Delete duplicate entries
all_news = filter.detect_duplicate(all_news)

# Create data base using SQL Lite
logger.info(f"Total items collected: {len(all_news)}")
db.upload_data_base(all_news)
