# Import necessary libraries
import sqlite3 as db
import pandas as pd
import os
from error_log import setup_logger
import hashlib

# Setup logger for debugging
logger = setup_logger(__name__)
logger.info("Running data base creation and csv exportation.")

# Function to generate hash for each article
def generate_hash(title, url, description):
    # Combine title, url, and description to create a unique string
    data = f"{title}{url}{description}"
    return hashlib.sha256(data.encode()).hexdigest()

def upload_data_base(list):
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
        hash TEXT UNIQUE,
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
        article_hash = generate_hash(item.get("title"), item.get("url"), item.get("description"))
        
        
        # Insert data into the table along with the hash
        cn.execute("""
            INSERT OR IGNORE INTO rss_feeds (hash, title, description, date, url, source, country, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (
            article_hash,
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

    # Close the connection and cursor
    cn.close()
    conn.close()

  