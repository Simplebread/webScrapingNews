import sqlite3 as db
import pandas as pd

def upload_data_base(list):
    # Create datbase connetion and cursor
    conn = db.connect('sqlite.db')
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
        cn.execute("""
            INSERT INTO rss_feeds (title, description, date, url, source, country, category)
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
    
    # Output as CSV file for viewing
    df.to_csv("news.csv", index=False, encoding='utf-8')    
    
    # Close the connection and cursor
    cn.close()
    conn.close()

  