# ========================================================================================
# config.py
#
# FILE OVERVIEW:
# This file acts as the central configuration hub for the entire application.
# It does not contain any executable logic. Instead, it stores all the key settings,
# lists, and data mappings in one easy-to-find place. This design makes the
# scraper highly configurable, as you can add new feeds or change keywords
# without touching the core application code.
# ========================================================================================

# --- Network Configuration ---

# Defines the User-Agent string for all network requests.
# This makes our script look like a standard web browser, which is more
# respectful to servers and helps avoid being blocked.
user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# --- Spacy Configuration ---

# Categories for RSS in which spacy will pick on
candidate_categories = ["Politics", "Business", "Technology", "Sports", "Health", "Entertainment", "World News"]
is_historical = False
start_date = "2025-01-01"
end_date = "2025-02-02"

# --- RSS Feed Definitions ---

# A list of dictionaries, where each dictionary represents one RSS feed to be scraped.
# - "url": The web address of the RSS feed.
# - "country": The default country for this source. Can be None if it needs to be detected.
# - "source": The name of the news publisher (e.g., "BBC").
# - "category": The default category. Can be None if it needs to be detected.
rss_feeds = [
    # -----
    {
        "url": "https://feeds.bbci.co.uk/news/uk/rss.xml",
        "country": "United Kingdom",
        "source": "BBC",
        "category": None
    },
    {
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
        "country": None,
        "source": "BBC",
        "category": "International"
    },
    {
        "url": "https://feeds.bbci.co.uk/news/health/rss.xml",
        "country": None,
        "source": "BBC",
        "category": "Health"
    },
    {
        "url": "https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
        "country": None,
        "source": "BBC",
        "category": None
    },
    # -----
    {
        "url": "https://www.cbc.ca/webfeed/rss/rss-canada",
        "country": None,
        "source": "CBC",
        "category": None
    },
    # -----
    {
        "url": "https://www.aljazeera.com/xml/rss/all.xml",
        "country": None,
        "source": "Al Jazeera",
        "category": None
    },
    # -----
    {
        "url": "https://abcnews.go.com/abcnews/topstories",
        "country": None,
        "source": "ABC",
        "category": None
    },
    {
        "url": "https://abcnews.go.com/abcnews/technologyheadlines",
        "country": None,
        "source": "ABC",
        "category": "Technology"
    },
    # -----
    {
        "url": "https://www.nippon.com/en/rss-all/",
        "country": "Japan",
        "source": "Nippon.com",
        "category": None
    },
    # -----
    {
        "url": "https://www.abc.net.au/news/feed/2942460/rss.xml",
        "country": "Australia",
        "source": "ABC Australia",
        "category": None
    },
    {
        "url": "https://www.abc.net.au/news/feed/45924/rss.xml",
        "country": "Australia",
        "source": "ABC Australia",
        "category": None
    },
    {
        "url": "https://www.abc.net.au/local/rss/sydney/news.xml",
        "country": "Australia",
        "source": "ABC Australia",
        "category": None
    },
    # -----
    {
        "url": "https://mexiconewsdaily.com/feed/",
        "country": "Mexico",
        "source": "Mexico News Daily",
        "category": None
    },
    # -----
    {
        "url": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
        "country": None,
        "source": "Times of India",
        "category": None
    },
    {
        "url": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
        "country": "India",
        "source": "Times of India",
        "category": None
    },
    {
        "url": "https://timesofindia.indiatimes.com/rssfeeds/54829575.cms",
        "country": "India",
        "source": "Times of India",
        "category": "Sport"
    },
    {
        "url": "https://indianexpress.com/section/opinion/40-years-ago/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/india/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/politics/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": "Politics"
    },
    {
        "url": "https://indianexpress.com/section/business/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/world/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/technology/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": "Technology"
    },
    {
        "url": "https://indianexpress.com/section/sports/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/entertainment/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/explained/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/opinion/editorials/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    {
        "url": "https://indianexpress.com/section/cities/feed/",
        "country": "India",
        "source": "The Indian Express",
        "category": None
    },
    # -----
    {
        "url": "https://www.france24.com/en/france/rss",
        "country": "France",
        "source": "France24",
        "category": None
    }
]

