import sqlite3
from .utils import generate_short_id

DB_NAME = "urls.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id TEXT PRIMARY KEY,
            original_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_url(original_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    short_id = generate_short_id()
    cursor.execute("INSERT INTO urls (id, original_url) VALUES (?, ?)", (short_id, original_url))
    
    conn.commit()
    conn.close()
    
    return short_id

def get_url(short_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT original_url FROM urls WHERE id = ?", (short_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    return row[0] if row else None
