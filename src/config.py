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

# Import necessary libraries
import json
from pathlib import Path

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
    "Politics", "Elections", "Business", "Technology", "Health", "Science",
    "Sports", "Entertainment", "Culture", "Environment",
    "Legal", "Social Issues", "Education", "Human Rights", "Conflict"
]
# Run conditions
is_historical = False
start_date = "2025-01-01"
end_date = "2025-02-02"
time=3

# --- RSS Feed Definitions ---

# A list of dictionaries, where each dictionary represents one RSS feed to be scraped.
def load_feeds(fname):
    return json.loads(Path(fname).read_text())

rss_feeds = []
# for file in Path("rss_configs").glob("*.json"):
rss_file = Path("rss_configs") / "foreign_language.json"
rss_feeds = load_feeds(rss_file)

# ========================================================================================
# --- KEYWORD DICTIONARIES FOR FALLBACK SYSTEM ---
# These lists are used ONLY if the primary NLP model fails to make a detection.
# They are designed to catch obvious cases.
# ========================================================================================

# --- Country Keyword Dictionary ---
# A dictionary used to automatically detect the country of an article as a backup.

key_word_country = {}
country_file = Path("key_words_config") / "country.json"
key_word_country = load_feeds(country_file)

# --- Category Keyword Dictionary ---
# A dictionary used to automatically detect the category of an article as a backup.
key_word_category = {}
category_file = Path("key_words_config") / "category.json"
key_word_category = load_feeds(category_file)

