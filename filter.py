# Import necessary libraries
import config as config
import parser as parser

# Filtering using keywords
def filtered_list(url, source, country, category):
    print(f"Fetching: {url}")

    items = parser.get_rss_items(url)
    filtered_data = []

    # Fetch data from the title tag
    for item in items:
        title = item.find("title").text if item.find("title") else ""
        description = item.find("description").text if item.find("description") else ""

        # Detect country and category dynamically
        if country == None:
            detected_country = detect_country(title, description)
        else:
            detected_country = country

        if category == None:
            detected_category = detect_category(title, description)
        else:
            detected_category = category

        # print(f"Detected Country: {detected_country}")
        # print(f"Detected Category: {detected_category}")

        filtered_data.append({
            "title": title,
            "description": description,
            "date": item.find("pubDate").text if item.find("pubDate") else "",
            "url": item.find("link").text if item.find("link") else "",
            "source": source,
            "country": detected_country,
            "category": detected_category
        })
    return filtered_data

def detect_country(title, description):
    content = f"{title} {description}".lower()
    # Add coutry to check the content with the country's name itself
    for country, keywords in config.key_word_country.items():
        for keyword in keywords:
            if keyword.lower() in content:
                print(f"  [DEBUG] Found country keyword '{keyword}' for '{country}'") # Optional: more detailed debug
                return country
    return "Unknown"

def detect_category(title, description):
    content = f"{title} {description}".lower()
    # Add coutry to check the content with the country's name itself
    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            if keyword.lower() in content:
                print(f"  [DEBUG] Found category keyword '{keyword}' for '{category}'") # Optional: more detailed debug
                return category
    return "General"