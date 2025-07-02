# ========================================================================================
# historical.py
#
# FILE OVERVIEW:
# This module is a specialized client for interacting with the Internet Archive's
# Wayback Machine. Its sole purpose is to handle historical data scraping. It finds
# all available snapshots (mementos) for a given URL within a specific date range
# and downloads the raw, original content of each one for processing.
# ========================================================================================

# Import necessary libraries
import wayback
from datetime import datetime
from error_log import setup_logger
import time
import config
import parser

# Setup logger for debugging
logger = setup_logger(__name__)


# In historical.py

def fetch_historical_documents(url, start_date, end_date):
    """
    Finds and downloads all historical RSS feed snapshots for a URL within a date range.
    It loops through each found snapshot, fetches its original content, and passes it
    to the parser.
    """
    logger.info(f"Searching for snapshots of '{url}' from {start_date} to {end_date}")

    # --- Client Setup ---
    # 1. Initialize the Wayback Machine client.
    client = wayback.WaybackClient()
    # 2. Set a browser-like User-Agent on the client's underlying session.
    # This is the correct way to set headers for this specific library.
    client.session.headers['User-Agent'] = config.user_agent['User-Agent']

    # --- API Search ---
    try:
        # Ask the Wayback Machine's CDX API for all snapshots of the URL.
        # The 'from_date' and 'to_date' parameters filter the results on the server side.
        snapshots = client.search(
            url,
            from_date=datetime.strptime(start_date, "%Y-%m-%d"),
            to_date=datetime.strptime(end_date, "%Y-%m-%d")
        )
    except Exception as e:
        logger.error(f"Failed to search for snapshots for {url}: {e}")
        return [] # Return an empty list if the initial search fails.

    # Prepare to collect the articles we find.
    all_found_items = []
    snapshot_count = 0

    # Loop through every snapshot record we found.
    for record in snapshots:
        snapshot_count += 1
        logger.info(f"Processing snapshot #{snapshot_count} from {record.timestamp.isoformat()}")

        try:
            # Request the original, raw file ("memento") for this snapshot.
            client.session.timeout = 60 # Set a 60-second timeout for the download.
            memento = client.get_memento(record, mode=wayback.Mode.original)

            # Pass the downloaded raw content to our parser.
            items = parser.parse_rss_content(memento.content, source_url=record.raw_url)

            if items:
                logger.info(f"Successfully parsed {len(items)} items from this snapshot.")
                all_found_items.extend(items)
            else:
                logger.warning(f"No usable <item> tags found in this snapshot.")

        except Exception as e:
            # Catch any other errors during download/processing and log them without crashing.
            logger.error(f"An unexpected error occurred processing memento {record.raw_url}: {e}")

        # Pause between request to stop rate limiting and maximum requests
        logger.info("Pausing for 3 seconds...")
        time.sleep(config.time)

    logger.info(f"Finished processing {snapshot_count} snapshots for {url}.")
    return all_found_items