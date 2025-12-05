import sqlite3
import os

# Create database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# Insert sample users
users = [
    ('admin', 'sup3r_s3cr3t_p@ssw0rd!', 'administrator'),
    ('john', 'john123', 'user'),
    ('sarah', 'sarah456', 'user'),
    ('guest', 'guest', 'guest')
]

cursor.executemany('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', users)

# Create flags table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flags (
        id INTEGER PRIMARY KEY,
        flag_text TEXT NOT NULL
    )
''')

# Read flag - with better error handling
flag = 'FLAG{1nj3ct10n_1s_th3_qu33n_0f_vuln5}'
if os.path.exists('flag.txt'):
    with open('flag.txt', 'r') as f:
        flag_content = f.read().strip()
        if flag_content:
            flag = flag_content

cursor.execute('INSERT INTO flags (flag_text) VALUES (?)', (flag,))

conn.commit()
conn.close()

print("✅ Database initialized successfully!")
print(f"🚩 Flag stored: {flag}")
print("👤 Admin credentials: admin / sup3r_s3cr3t_p@ssw0rd!")
print("📊 4 users created")