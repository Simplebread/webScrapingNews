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
candidate_categories = [
    "Politics", "Elections", "Business", "Finance", "Technology", "Health", "Science",
    "Sports", "Entertainment", "Culture", "World News", "Environment", "Climate Change",
    "Legal", "Social Issues", "Education", "Human Rights", "Conflict"
]
# Run conditions
is_historical = False
start_date = "2025-01-01"
end_date = "2025-02-02"
time=3

# --- RSS Feed Definitions ---

# A list of dictionaries, where each dictionary represents one RSS feed to be scraped.
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

# ========================================================================================
# --- KEYWORD DICTIONARIES FOR FALLBACK SYSTEM ---
# These lists are used ONLY if the primary NLP model fails to make a detection.
# They are designed to catch obvious cases.
# ========================================================================================

# --- Country Keyword Dictionary ---
# A dictionary used to automatically detect the country of an article as a backup.
key_word_country = {
    "United States": [
        "US", "U.S.", "USA", "America", "American", "Washington D.C.", "White House",
        "Congress", "Senate", "Pentagon", "New York", "California", "Texas", "Florida",
        "Biden", "Trump", "Federal Reserve", "FBI", "CIA", "NASDAQ", "Wall Street"
    ],
    "United Kingdom": [
        "UK", "U.K.", "Britain", "British", "England", "London", "Scotland", "Wales",
        "Northern Ireland", "Parliament", "Downing Street", "NHS", "Sunak", "Starmer",
        "Brexit", "Westminster", "Bank of England"
    ],
    "Canada": [
        "Canada", "Canadian", "Ottawa", "Toronto", "Vancouver", "Montreal", "Quebec",
        "Trudeau", "Parliament Hill", "RCMP"
    ],
    "Australia": [
        "Australia", "Australian", "Canberra", "Sydney", "Melbourne", "Aussie",
        "Albanese", "Down Under", "ASX"
    ],
    "China": [
        "China", "Chinese", "Beijing", "Shanghai", "Xi Jinping", "CCP",
        "Communist Party", "Yuan", "Hong Kong", "Taiwan", "Shenzhen", "Huawei"
    ],
    "India": [
        "India", "Indian", "New Delhi", "Mumbai", "Modi", "BJP", "Congress Party",
        "Bollywood", "Rupee", "Bangalore", "Kolkata"
    ],
    "Russia": [
        "Russia", "Russian", "Moscow", "Kremlin", "Putin", "Siberia", "Gazprom",
        "Soviet", "St. Petersburg", "FSB", "Rouble"
    ],
    "Ukraine": [
        "Ukraine", "Ukrainian", "Kyiv", "Zelenskyy", "Donbas", "Crimea", "Lviv",
        "Kharkiv", "Odessa"
    ],
    "Germany": [
        "Germany", "German", "Berlin", "Merkel", "Scholz", "Bundesliga",
        "Frankfurt", "Munich", "Bundestag", "Deutsche Bank"
    ],
    "France": [
        "France", "French", "Paris", "Macron", "Eiffel Tower", "Le Pen",
        "Marseille", "Ligue 1", "Elysée Palace"
    ],
    "Japan": [
        "Japan", "Japanese", "Tokyo", "Kyoto", "Kishida", "Yen", "Nintendo", "Sony",
        "Toyota", "Nikkei", "Diet"
    ],
    "Brazil": [
        "Brazil", "Brazilian", "Brasília", "Rio de Janeiro", "São Paulo",
        "Lula da Silva", "Amazon rainforest", "Bolsonaro"
    ],
    "South Africa": [
        "South Africa", "South African", "Pretoria", "Cape Town", "Johannesburg",
        "Ramaphosa", "ANC", "Apartheid", "Rand"
    ],
    "Israel": [
        "Israel", "Israeli", "Jerusalem", "Tel Aviv", "Netanyahu", "Knesset",
        "Gaza", "West Bank", "IDF", "Mossad", "Palestine", "Palestinian"
    ],
    "Iran": [
        "Iran", "Iranian", "Tehran", "Khamenei", "Persian", "IRGC", "Rial"
    ],
    "Saudi Arabia": [
        "Saudi Arabia", "Saudi", "Riyadh", "Mecca", "MBS", "Mohammed bin Salman",
        "Aramco", "OPEC"
    ],
    "Nigeria": [
        "Nigeria", "Nigerian", "Abuja", "Lagos", "Boko Haram", "Naira"
    ],
    "Mexico": [
        "Mexico", "Mexican", "Mexico City", "Tijuana", "Cancun", "Cartel", "Peso"
    ],
    "South Korea": [
        "South Korea", "Korean", "Seoul", "Samsung", "Hyundai", "K-Pop", "DMZ",
        "Yoon Suk Yeol"
    ],
    "Turkey": [
        "Turkey", "Turkish", "Ankara", "Istanbul", "Erdogan", "Lira", "Anatolia"
    ]
}

# --- Category Keyword Dictionary ---
# A dictionary used to automatically detect the category of an article as a backup.
key_word_category = {
    "Politics": [
        "election", "government", "parliament", "vote", "political", "policy",
        "White House", "Downing Street", "senate", "congress", "law", "bill",
        "president", "prime minister", "chancellor", "treaty", "diplomacy",
        "Democrat", "Republican", "Conservative", "Labour", "legislation"
    ],
    "Business": [
        "business", "economy", "market", "stock", "shares", "nasdaq", "dow jones",
        "company", "corporate", "finance", "earnings", "revenue", "profit",
        "inflation", "interest rate", "CEO", "IPO", "merger", "acquisition",
        "investment", "trade", "commerce", "fiscal"
    ],
    "Technology": [
        "technology", "tech", "AI", "artificial intelligence", "smartphone", "Apple",
        "Google", "Microsoft", "Amazon", "Meta", "Facebook", "software", "hardware",
        "internet", "startup", "iPhone", "Android", "semiconductor", "chip",
        "data center", "cybersecurity", "app", "platform"
    ],
    "Sports": [
        "sports", "football", "basketball", "soccer", "tennis", "cricket", "olympics",
        "world cup", "championship", "league", "match", "game", "player", "team",
        "NBA", "NFL", "Premier League", "MLB", "NHL", "athlete", "score", "stadium"
    ],
    "Health": [
        "health", "medicine", "hospital", "doctor", "NHS", "CDC", "WHO", "pandemic",
        "virus", "vaccine", "disease", "treatment", "mental health", "healthcare",
        "pharma", "clinical trial", "medical"
    ],
    "Science": [
        "science", "research", "study", "discovery", "space", "NASA", "ESA",
        "physics", "chemistry", "biology", "astronomy", "particle", "quantum",
        "genetics", "archaeology", "geology"
    ],
    "Environment": [
        "environment", "climate change", "global warming", "carbon emissions",
        "renewable energy", "solar", "wind", "conservation", "pollution",
        "endangered species", "sustainability", "COP28"
    ],
    "Entertainment": [
        "entertainment", "movie", "film", "TV", "television", "music", "album",
        "song", "concert", "celebrity", "Hollywood", "Bollywood", "actor",
        "actress", "box office", "Netflix", "Disney", "Grammys", "Oscars"
    ],
    "Culture": [
        "culture", "art", "museum", "exhibit", "theatre", "literature", "book",
        "author", "heritage", "tradition", "fashion", "food", "cuisine"
    ],
    "Conflict": [
        "conflict", "war", "battle", "military", "troops", "invasion", "airstrike",
        "ceasefire", "insurgency", "refugee", "humanitarian crisis"
    ],
    "Legal": [
        "legal", "court", "supreme court", "lawsuit", "trial", "verdict",
        "prosecutor", "judge", "attorney", "justice department"
    ]
}