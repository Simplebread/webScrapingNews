# ========================================================================================
# run_scraper.py
#
# FILE OVERVIEW:
# This is the main entry point for the entire application. Its job is to start the
# scraping process, loop through the news sources defined in config.py, call the
# appropriate modules to fetch and filter the data, and then hand off the final
# list of articles to the database module for saving. It also handles the main
# flag for switching between "live" mode and "historical" mode.
# ========================================================================================

# Import necessary modules from your project
import config
import filter
import data_base
from error_log import setup_logger

# --- Initial Setup ---

# Set up a logger for this specific file.
logger = setup_logger(__name__)

# This list will hold all the news articles collected from all sources.
all_news = []


# --- Main Application Loop ---

# Loop through each news feed dictionary defined in the 'rss_feeds' list in config.py.
for feed in config.rss_feeds:
    try:
        # --- Scraping Mode Configuration ---
        # This section determines whether to fetch live news or historical news.
        # True for historical scraping false for the latter
        is_historical = True
        start_date = "2025-01-01"
        end_date = "2025-02-02"

        # Call the main filtering function, which acts as the entry point for the core logic.
        # It passes all the necessary information for a single feed to be processed.
        results = filter.filtered_list(
            url=feed["url"],
            source=feed["source"],
            pre_defined_country=feed["country"],
            pre_defined_category=feed["category"],
            is_historical=is_historical,
            start_date=start_date,
            end_date=end_date
        )
        
        # Add the list of articles found from this one feed to our main collection.
        all_news.extend(results)

    except Exception as e:
        # A general catch-all to ensure that if one feed fails completely,
        # the entire program doesn't crash. It logs the error and moves to the next feed.
        logger.error(f"A critical error occurred while processing the feed {feed['ur' \
        'l']}: {str(e)}")


# --- Final Data Processing ---

# After looping through all feeds, remove any duplicate articles from the entire collection.
all_news = filter.detect_duplicate(all_news)


# --- Database and Export ---

# Log the total number of unique articles collected before saving.
logger.info(f"Total unique items collected from all sources: {len(all_news)}")

# Pass the final, clean list of articles to the database module to be saved.
data_base.upload_data_base(all_news)

logger.info("Scraping process completed successfully.")
