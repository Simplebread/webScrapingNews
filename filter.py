# Import necessary libraries
import config as config
import parser as parser

# Filtering using keywords
def filtered_list(url, source):
    items = parser.get_rss_items(url)
    filtered_data = []

    # 
    for item in items:
        title = item.find("title").text if item.find("title") else ""
        description = item.find("description").text if item.find("description") else ""

        # Detect country and category dynamically
        country = detect_country(title, description)
        category = detect_category(title, description)

        filtered_data.append({
            "title": title,
            "description": description,
            "date": item.find("pubDate").text if item.find("pubDate") else "",
            "url": item.find("link").text if item.find("link") else "",
            "source": source,
            "country": country,
            "category": category
        })
    return filtered_data

def detect_country(title, description):
    content = f"{title} {description}".lower()

    for country, keywords in config.key_word_country.items():
        for keyword in keywords:
            if keyword.lower() in content:
                return country
    return "Unknown"

def detect_category(title, description):
    content = f"{title} {description}".lower()

    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            if keyword.lower() in content:
                return category
    return "General"