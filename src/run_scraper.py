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
        # If you want to scrape historical data, set historical=True and provide date range
        historical = True  # Set to True if historical data is needed
        start_date = "2023-06-01"  # Set the start date if historical is True
        end_date = "2023-06-10"    # Set the end date if historical is True
        
        # Inputs data from config.py to be processed
        results = filter.filtered_list(
            feed["url"], 
            feed["source"], 
            feed["country"], 
            feed["category"], 
            historical=historical,  # Pass the historical flag
            start_date=start_date,  # Pass start_date for historical
            end_date=end_date       # Pass end_date for historical
        )
        all_news.extend(results)
    except Exception as e:
        # Debugging
        logger.error(f"Skipping {feed['url']} due to {str(e)}")

# Delete duplicate entries
all_news = filter.detect_duplicate(all_news)

# Create data base using SQL Lite
db.upload_data_base(all_news)
