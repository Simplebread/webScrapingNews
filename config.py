# RSS Links for news
rss_feeds = [
    {
        "url": "https://feeds.bbci.co.uk/news/uk/rss.xml",
        "country": "United Kingdom",
        "source": "BBC",
        "category": None
    },
    {
        "url": "https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
        "country": None,
        "source": "BBC",
        "category": None
    },
    {
        "url": "https://www.cbc.ca/webfeed/rss/rss-canada",
        "country": None,
        "source": "CBC",
        "category": None
    },

    # World has repeating news articles

    # {
    #     "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
    #     "country": "",
    #     "source": "BBC",
    #     "category": "International"
    # },
    {
        "url": "https://feeds.bbci.co.uk/news/health/rss.xml",
        "country": None,
        "source": "BBC",
        "category": "health"
    },
    {
        "url": "https://www.aljazeera.com/xml/rss/all.xml",
        "country": None,
        "source": "Al Jazeera",
        "category": None
    },
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
    }
]

# Categories with keys and dictionaries
key_word_category = {
    "Technology": [
        "tech", "apple", "AI", "robot", "software",
        "cloud", "data", "cyber", "quantum", "satellite",
        "drone", "processor", "chip", "emissions", "robotics"
    ],
    "Health": [
        "health", "vaccine", "covid", "covid-19",
        "mental", "medicine", "pandemic", "disease",
        "doctor", "hospital", "cancer", "diabetes"
    ],
    "Politics": [
        "election", "government", "policy", "senate",
        "democracy", "parliament", "congress", "law",
        "UN", "NATO", "tariff", "sanction", "budget",
        "campaign"
    ],
    "Sports": [
        "football", "soccer", "olympics", "NBA", "tennis",
        "cricket", "rugby", "golf", "F1", "cup", "league"
    ]
}

# Key words for countries
key_word_country = {
    "United Kingdom": [
        "UK", "Britain", "British", "London", "Rishi Sunak", "Downing Street", 
        "England", "Scotland", "Wales", "Northern Ireland", "Westminster"
    ],
    "United States": [
        "USA", "US", "America", "American", "White House", "Biden", "Trump", 
        "Washington", "New York", "Los Angeles", "Pentagon", "Capitol", "Senate"
    ],
    "Canada": [
        "Canada", "Canadian", "Ottawa", "Toronto", "Vancouver", "Trudeau", 
        "Alberta", "Quebec", "Liberal Party", "RCMP"
    ],
    "China": [
        "China", "Chinese", "Beijing", "Xi Jinping", "CCP", "Shanghai", 
        "Hong Kong", "Taiwan", "Great Wall", "Renminbi"
    ],
    "Myanmar": [
        "Myanmar", "Burma", "Burmese", "Yangon", "Naypyidaw", "Min Aung Hlaing", 
        "NLD", "Aung San Suu Kyi", "Tatmadaw", "Sagaing", "Junta"
    ],
    "Russia": [
        "Russia", "Russian", "Moscow", "Putin", "Kremlin", "Ukraine war", 
        "Wagner", "Red Square", "FSB", "Donetsk"
    ],
    "India": [
        "India", "Indian", "Delhi", "Modi", "Mumbai", "Hindustan", "BJP", 
        "Kolkata", "Kerala", "Himalayas"
    ],
    "France": [
        "France", "French", "Paris", "Macron", "Élysée", "Louvre", "Marseille", 
        "Provence", "Bastille", "Sorbonne"
    ],
    "Germany": [
        "Germany", "German", "Berlin", "Scholz", "Bundestag", "Munich", 
        "Frankfurt", "Hamburg", "Bavaria"
    ],
    "Japan": [
        "Japan", "Japanese", "Tokyo", "Yen", "Fumio Kishida", "Osaka", 
        "Kyoto", "Shinkansen", "Samurai", "Anime"
    ],
    "South Korea": [
        "South Korea", "Korea", "Korean", "Seoul", "Yoon Suk-yeol", 
        "Samsung", "Hyundai", "K-pop", "DMZ", "Pyongyang"
    ],
    "Australia": [
        "Australia", "Australian", "Canberra", "Sydney", "Melbourne", 
        "Albanese", "Outback", "Down Under", "ANZAC"
    ],
    "Brazil": [
        "Brazil", "Brasília", "Rio de Janeiro", "São Paulo", "Lula", 
        "Amazon", "Carnival", "Favelas", "Petrobras"
    ],
    "South Africa": [
        "South Africa", "African", "Johannesburg", "Cape Town", 
        "Ramaphosa", "ANC", "Apartheid", "Zulu", "Durban"
    ],
    "Ukraine": [
        "Ukraine", "Ukrainian", "Kyiv", "Zelensky", "Donbas", 
        "Lviv", "Dnipro", "Kharkiv", "Mariupol"
    ],
    "Italy": [
        "Italy", "Italian", "Rome", "Milan", "Florence", "Naples", 
        "Pasta", "Colosseum", "Meloni", "Vatican"
    ],
    "Mexico": [
        "Mexico", "Mexican", "Mexico City", "AMLO", "Cartel", 
        "Guadalajara", "Tijuana", "Peso", "Cancun"
    ],
    "Philippines": [
        "Philippines", "Filipino", "Manila", "Duterte", "Marcos", 
        "Visayas", "Mindanao", "Tagalog", "Cebu", "Davao"
    ]
}
