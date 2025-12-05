from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# This will be the flag returned on successful SQL injection
FLAG = "CTF{injection_master_flag_placeholder}"

# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Create a users table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')

    # Insert a fake admin user (normal login attempts should fail)
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecret')")
    conn.commit()
    conn.close()

# Initialize DB when the server starts
init_db()

# Login route (UI only for now)
@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # For now: simple placeholder, no SQL query yet
        message = "Invalid credentials."

    return render_template_string("""
        <h1>Injection Master</h1>
        <p>Login to access the admin panel:</p>
        <form method="POST">
            <label>Username:</label><br>
            <input name="username"><br><br>
            <label>Password:</label><br>
            <input name="password" type="password"><br><br>
            <button type="submit">Login</button>
        </form>
        <p>{{ message }}</p>
    """, message=message)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
