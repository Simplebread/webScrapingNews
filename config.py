# RSS Links for news
rss_feeds = [
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
    #
    {
        "url": "https://www.cbc.ca/webfeed/rss/rss-canada",
        "country": None,
        "source": "CBC",
        "category": None
    },
    #
    {
        "url": "https://www.aljazeera.com/xml/rss/all.xml",
        "country": None,
        "source": "Al Jazeera",
        "category": None
    },
    #
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
    #
    {
        "url": "https://www.nippon.com/en/rss-all/",
        "country": "Japan",
        "source": "Nippon.com",
        "category": None
    },
    #
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
    #
    {
        "url": "https://mexiconewsdaily.com/feed/",
        "country": "Mexico",
        "source": "Mexico News Daily",
        "category": None
    },
    #
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
    #
    {
        "url": "https://www.france24.com/en/france/rss",
        "country": "France",
        "source": "France24",
        "category": None
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
    ],
    "Indonesia": [
        "Indonesia", "Indonesian", "Jakarta", "Jokowi", "Bali", 
        "Java", "Sumatra", "Sulawesi", "Garuda", "Rupiah"
    ],
    "Pakistan": [
        "Pakistan", "Pakistani", "Islamabad", "Karachi", "Lahore", 
        "Imran Khan", "Punjab", "Urdu", "Khyber", "Sindh"
    ],
    "Bangladesh": [
        "Bangladesh", "Bangladeshi", "Dhaka", "Sheikh Hasina", 
        "Chittagong", "Bengali", "Padma", "Rohingya"
    ],
    "Turkey": [
        "Turkey", "Turkish", "Ankara", "Istanbul", "Erdogan", 
        "Bosporus", "Lira", "Hagia Sophia", "Atatürk"
    ],
    "Saudi Arabia": [
        "Saudi Arabia", "Saudi", "Riyadh", "MBS", "Mecca", "Medina", 
        "Aramco", "Hajj", "Oil", "Quran"
    ],
    "Iran": [
        "Iran", "Tehran", "Persian", "Ayatollah", "Khamenei", 
        "Revolutionary Guard", "Shia", "Sanctions", "Nuclear"
    ],
    "Israel": [
        "Israel", "Israeli", "Jerusalem", "Tel Aviv", "Netanyahu", 
        "IDF", "Gaza", "West Bank", "Hebrew", "Knesset"
    ],
    "Thailand": [
        "Thailand", "Thai", "Bangkok", "Chiang Mai", "Bhumibol", 
        "Prayut", "Baht", "Phuket", "Siam"
    ],
    "Vietnam": [
        "Vietnam", "Vietnamese", "Hanoi", "Ho Chi Minh", 
        "Da Nang", "Communist Party", "Mekong", "Dong", "Saigon"
    ],
    "Argentina": [
        "Argentina", "Argentinian", "Buenos Aires", "Messi", 
        "Patagonia", "Peso", "Maradona", "Tango"
    ],
    "Nigeria": [
        "Nigeria", "Nigerian", "Abuja", "Lagos", "Buhari", 
        "Yoruba", "Hausa", "Igbo", "Naira", "Boko Haram"
    ],
    "Egypt": [
        "Egypt", "Egyptian", "Cairo", "Sisi", "Nile", "Pyramid", 
        "Pharaoh", "Alexandria", "Giza", "Suez"
    ],
    "Spain": [
        "Spain", "Spanish", "Madrid", "Barcelona", "Sánchez", 
        "Catalonia", "Andalusia", "Basque", "Euro", "Iberia"
    ],
    "Poland": [
        "Poland", "Polish", "Warsaw", "Duda", "Krakow", 
        "Solidarity", "Gdańsk", "Zloty", "PiS"
    ],
    "Malaysia": [
        "Malaysia", "Malaysian", "Kuala Lumpur", "Anwar", 
        "Sabah", "Sarawak", "Malay", "Ringgit"
    ],
    "Vietnam": [
        "Vietnam", "Vietnamese", "Hanoi", "Ho Chi Minh", 
        "Da Nang", "Saigon", "Mekong", "Dong", "Communist Party"
    ],
    "Sweden": [
        "Sweden", "Swedish", "Stockholm", "Kristersson", 
        "Nobel", "IKEA", "Scandinavia", "Krona"
    ],
    "Norway": [
        "Norway", "Norwegian", "Oslo", "Støre", "Fjord", 
        "NATO", "Kroner", "Scandinavian"
    ],
    "Greece": [
        "Greece", "Greek", "Athens", "Tsipras", "Mitsotakis", "Acropolis",
        "Eurozone", "Olympics", "Aegean", "Parthenon"
    ],
    "Iraq": [
        "Iraq", "Iraqi", "Baghdad", "Mosul", "Basra", "Kurdistan",
        "Shiite", "Sunni", "Saddam Hussein", "Green Zone"
    ],
    "Syria": [
        "Syria", "Syrian", "Damascus", "Aleppo", "Assad", "Homs",
        "ISIS", "Kurds", "Idlib", "Golan"
    ],
    "Lebanon": [
        "Lebanon", "Lebanese", "Beirut", "Hezbollah", "Cedar", "Michel Aoun",
        "Port Explosion", "Hariri", "Tripoli"
    ],
    "Afghanistan": [
        "Afghanistan", "Afghan", "Kabul", "Taliban", "Pashtun", "Hazaras",
        "Burqa", "NATO withdrawal", "Ashraf Ghani"
    ],
    "North Korea": [
        "North Korea", "Pyongyang", "Kim Jong-un", "DPRK", "Demilitarized Zone",
        "Nuclear test", "Hermit Kingdom", "Missile launch"
    ],
    "Colombia": [
        "Colombia", "Colombian", "Bogotá", "Medellín", "Cali", "FARC",
        "Cartel", "Peso", "Duque", "Petro"
    ],
    "Venezuela": [
        "Venezuela", "Venezuelan", "Caracas", "Maduro", "Bolivar", "Chávez",
        "PDVSA", "Hyperinflation", "Opposition protest"
    ],
    "Chile": [
        "Chile", "Chilean", "Santiago", "Pinochet", "Boric", "Andes",
        "Constitutional reform", "Valparaíso"
    ],
    "Peru": [
        "Peru", "Peruvian", "Lima", "Machu Picchu", "Quechua", "Pedro Castillo",
        "Cusco", "Andean", "Inca"
    ]
}

