# Import necessary libraries
import config as config
import parser as parser
from bs4 import BeautifulSoup

# Filter using keywords
def filtered_list(url, source, country, category):

    # Debugging
    print(f"Fetching: {url}")

    # Create necesary variables 
    items = parser.get_rss_items(url)
    filtered_data = []

    # Fetch data from the title tag
    for item in items:
        title = item.find("title").text if item.find("title") else ""
        description = item.find("description").text if item.find("description") else ""

        # Parse again to get rid of complicated ugly news RSS inside description (CBC)
        soup = BeautifulSoup(description, "html.parser")
        for tag in soup(["img", "style", "script"]):
            tag.decompose()
        description = soup.get_text(separator=" ", strip=True)

        # Detect country and category dynamically
        if country == None:
            detected_country = detect_country(title, description)
        else:
            detected_country = country

        if category == None:
            detected_category = detect_category(title, description)
        else:
            detected_category = category

        # For debugging
        # print(f"[DEBUG] Detected Country: {detected_country}")
        # print(f"[DEBUG] Detected Category: {detected_category}")

        # Append all the data into the local variable which will be returned
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

# Function to detect country
def detect_country(title, description):
    content = f"{title} {description}".lower()
    # Check the values of the keys and comparing them for keywords
    for country, keywords in config.key_word_country.items():
        for keyword in keywords:
            if keyword.lower() in content:
                # For debugging
                print(f"[DEBUG] Found country keyword '{keyword}' for '{country}'")
                return country
    return "Unknown"

# Functino to detect category
def detect_category(title, description):
    content = f"{title} {description}".lower()
    # Check the values of the keys and comparing them for keywords
    for category, keywords in config.key_word_category.items():
        for keyword in keywords:
            if keyword.lower() in content:
                # For debugging
                # print(f"[DEBUG] Found category keyword '{keyword}' for '{category}'")
                return category
    return "General"

# Function to detect duplicate in news and article entries
def detect_duplicate(list):
    # Nested loop to go through the whole list
    new_list = list
    i = 0
    while i<len(new_list):
        j = i + 1
        while j<len(new_list):
            # Compares one title to everything in the list
            if new_list[i]["title"].strip().lower() == new_list[j]['title'].strip().lower():
                new_list.pop(j)
            else:
                j+=1
        i+=1
    return new_list


