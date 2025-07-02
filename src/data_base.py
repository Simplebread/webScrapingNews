# ========================================================================================
# data_base.py
#
# FILE OVERVIEW:
# This module is the final step in the pipeline. It is responsible for all
# interactions with the SQLite database. Its job is to take the final, cleaned
# list of articles, create a unique hash for each one, and then insert them into
# the database, efficiently ignoring any duplicates. It also exports the final
# database content to a CSV file for easy viewing.
# ========================================================================================

# Import necessary libraries
import sqlite3 as db
import pandas as pd
import os
from error_log import setup_logger
# import hashlib

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running data base creation and csv exportation.")

# Function to generate hash for each article
# def generate_hash(title, url, description):
#     """
#     Creates a unique and consistent SHA256 hash for an article.
#     This hash acts as a unique ID. By combining the title, URL, and description,
#     we ensure that even if one of these fields changes slightly, the hash will be different.
#     """
#     # Combine title, url, and description to create a unique string
#     data = f"{title}{url}{description}"
#     return hashlib.sha256(data.encode()).hexdigest()

def upload_data_base(list):
    """
    Connects to the SQLite database, creates the table if it doesn't exist,
    and inserts all the provided articles.
    """
    # Redirects the file back toward the data folder
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "sqlite.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Create datbase connetion and cursor
    conn = db.connect(db_path)
    cn = conn.cursor()


    # Create table
    cn.execute("""
        CREATE TABLE IF NOT EXISTS rss_feeds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        date TEXT,
        url TEXT,
        source TEXT,
        country TEXT,
        category TEXT
    )
    """)

    # Insert all_news data
    for item in list:
        # Generate the hash for the article
        # article_hash = generate_hash(item.get("title"), item.get("url"), item.get("description"))
        
        cn.execute("""
            INSERT OR IGNORE INTO rss_feeds (title, description, date, url, source, country, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, 
            (
            item.get("title"),
            item.get("description"),
            item.get("date"),
            item.get("url"),
            item.get("source"),
            item.get("country"),
            item.get("category")
            )
        )

    # Save changes
    conn.commit()
    
    # Read from database into DataFrame
    df = pd.read_sql_query("SELECT * FROM rss_feeds", conn)
    
    # Redirects the file back toward the data folder
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "news.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # Output as CSV file for viewing    
    df.to_csv(csv_path, index=False, encoding="utf-8")

    # Summary Statistic
    logger.info("Generating and exporting summary analytics...")
    
    # Category Summary
    category_summary_path = os.path.join(os.path.dirname(__file__), "..", "data", "category_summary.csv")
    category_counts = df['category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Article_Count']
    category_counts.to_csv(category_summary_path, index=False)
    logger.info(f"Successfully exported category summary to {category_summary_path}")

    # Country Summary
    country_summary_path = os.path.join(os.path.dirname(__file__), "..", "data", "country_summary.csv")
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Article_Count']
    country_counts.to_csv(country_summary_path, index=False)
    logger.info(f"Successfully exported country summary to {country_summary_path}")

    # Close the connection and cursor
    cn.close()
    conn.close()

  