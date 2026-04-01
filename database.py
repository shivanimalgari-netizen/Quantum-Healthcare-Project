import sqlite3

def create_db():
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        encrypted_data TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(data_list):
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    for data in data_list:
        cursor.execute("INSERT INTO patients (encrypted_data) VALUES (?)", (data,))

    conn.commit()
    conn.close()