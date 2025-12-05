from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# HTML Templates
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SecureBank Login</title>
    <style>
        body { 
            font-family: 'Segoe UI', Arial; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .container { 
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            width: 400px;
        }
        h1 { 
            color: #667eea;
            text-align: center;
            margin-bottom: 30px;
        }
        input { 
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #ddd;
            border-radius: 8px;
            box-sizing: border-box;
            font-size: 14px;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        button { 
            width: 100%;
            background: #667eea;
            color: white;
            border: none;
            padding: 14px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
        }
        button:hover { 
            background: #5568d3;
        }
        .error { 
            background: #fee;
            border: 1px solid #fcc;
            color: #c33;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 15px;
            text-align: center;
        }
        .hint {
            text-align: center;
            color: #999;
            font-size: 12px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏦 SecureBank Portal</h1>
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <div class="hint">Hint: Try guest/guest to test the system</div>
    </div>
</body>
</html>
'''

SUCCESS_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome - SecureBank</title>
    <style>
        body { 
            font-family: 'Segoe UI', Arial; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .container { 
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            width: 500px;
        }
        h1 { 
            color: #667eea;
            text-align: center;
        }
        .user-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .flag-box {
            background: #d4edda;
            border: 2px solid #28a745;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        .flag-text {
            font-family: 'Courier New', monospace;
            font-size: 18px;
            color: #155724;
            font-weight: bold;
        }
        a {
            display: block;
            text-align: center;
            color: #667eea;
            text-decoration: none;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ Login Successful!</h1>
        <div class="user-info">
            <p><strong>Username:</strong> {{ username }}</p>
            <p><strong>Role:</strong> {{ role }}</p>
        </div>
        {% if flag %}
            <div class="flag-box">
                <h2>🎉 Administrator Access Detected!</h2>
                <p>Here's your flag:</p>
                <p class="flag-text">{{ flag }}</p>
            </div>
        {% else %}
            <p style="text-align: center; color: #666;">
                Regular users don't have access to sensitive data.
            </p>
        {% endif %}
        <a href="/">← Back to Login</a>
    </div>
</body>
</html>
'''

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE, error=None)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    # VULNERABLE CODE - String concatenation allows SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(query)
        user = cursor.fetchone()
        
        if user:
            # Check if admin
            flag = None
            if user['role'] == 'administrator':
                cursor.execute("SELECT flag_text FROM flags LIMIT 1")
                flag_row = cursor.fetchone()
                if flag_row:
                    flag = flag_row[0]
            
            conn.close()
            return render_template_string(SUCCESS_PAGE, 
                                        username=user['username'], 
                                        role=user['role'],
                                        flag=flag)
        else:
            conn.close()
            return render_template_string(LOGIN_PAGE, 
                                        error="Invalid username or password")
    except Exception as e:
        return render_template_string(LOGIN_PAGE, 
                                    error=f"Database error: {str(e)}")

if __name__ == '__main__':
    # Initialize database if it doesn't exist
    if not os.path.exists('users.db'):
        import subprocess
        subprocess.run(['python', 'init_db.py'])
    
    app.run(host='0.0.0.0', port=5000, debug=False)