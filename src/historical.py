# Import necessary libraries
import wayback
from datetime import datetime
import requests
from error_log import setup_logger
import time
import config
import parser

# Setup logger for debugging
logger = setup_logger(__name__)


def fetch_historical_documents(url, start_date, end_date):
    logger.info(f"Searching for snapshots of '{url}' from {start_date} to {end_date}")
    
    # Create client
    client = wayback.WaybackClient()
    filtered_items = []
    snapshot_count = 0
    
    # Set up header and user-agent to pretend to be a browser
    client.session.headers['User-Agent'] = config.user_agent['User-Agent']

    # This generator will query the CDX API for snapshots in the date range
    try:
        snapshots = client.search(
            url,
            from_date=datetime.strptime(start_date, "%Y-%m-%d"),
            to_date=datetime.strptime(end_date, "%Y-%m-%d")
        )
    except Exception as e:
        logger.error(f"Failed to search for snapshots for {url}: {e}")
        return []

    # Update snapshot count in the wayback machine
    for record in snapshots:
        snapshot_count += 1
        logger.info(f"Fetching memento for snapshot from {record.timestamp.isoformat()}")

        try:
            # 'get_memento' fetches the original, raw content, bypassing the HTML wrapper.
            # Set the timeout directly on the session before the request.
            client.session.timeout = 60
            memento = client.get_memento(record, mode=wayback.Mode.original)
            
            # Now we pass the raw content to the parser
            items = parser.parse_rss_content(memento.content, source_url=record.raw_url)
            
            if items:
                logger.info(f"Successfully parsed {len(items)} items from snapshot.")
                filtered_items.extend(items)
            else:
                logger.warning(f"No <item> tags found in snapshot from {record.timestamp.isoformat()}. The content may be HTML or an error page.")

        except requests.exceptions.ReadTimeout:
            logger.error(f"Read timeout while fetching memento: {record.raw_url}. Skipping.")
        except Exception as e:
            logger.error(f"An unexpected error occurred fetching memento {record.raw_url}: {e}")

        # Pause to avoid max request limit
        logger.info("Pausing for 3 seconds...")
        time.sleep(3)
        
    logger.info(f"Finished processing {snapshot_count} snapshots for {url}.")
    return filtered_items