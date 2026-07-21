import sqlite3

# Connect to database
conn = sqlite3.connect("database/student.db")

# Create cursor
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    phone TEXT,
    email TEXT
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")