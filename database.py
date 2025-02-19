import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ice_cream.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    is_available BOOLEAN DEFAULT 1
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER,
    unit TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    allergy_concerns TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS allergens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

conn.commit()
conn.close()