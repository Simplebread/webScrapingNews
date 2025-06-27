from waybackpy import WaybackMachineCDXServerAPI
from parser import get_rss_items

# Function to get historical URLs from Wayback Machine
def get_historical_urls(url):
    cdx = WaybackMachineCDXServerAPI(url, user_agent="Mozilla/5.0")
    snapshots = cdx.snapshots()
    historical_urls = []

    for snapshot in snapshots:
        historical_urls.append(snapshot.archive_url)

    return historical_urls

# Function to fetch historical documents for a given URL within a specified range
def fetch_historical_documents(url, start_date, end_date):
    historical_urls = get_historical_urls(url)
    filtered_items = []

    for historical_url in historical_urls:
        # Fetch and parse content for each snapshot URL using parser.py
        items = get_rss_items(historical_url)  # Use your parser to process the snapshot content

        # Filter items by date (you can modify this to match specific date ranges)
        for item in items:
            pub_date_tag = item.find("pubDate")
            if pub_date_tag:
                pub_date = pub_date_tag.text.strip()

                # Only include items within the date range
                if start_date <= pub_date <= end_date:
                    filtered_items.append(item)
    
    return filtered_items
