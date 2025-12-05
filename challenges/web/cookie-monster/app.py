from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# Read flag from file
with open('flag.txt', 'r') as f:
    FLAG = f.read().strip()

# Simple HTML template
HOME_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Cookie Monster's Vault</title>
    <style>
        body { font-family: Arial; background: #1a1a2e; color: #eee; text-align: center; padding: 50px; }
        .container { max-width: 600px; margin: auto; background: #16213e; padding: 30px; border-radius: 10px; }
        button { background: #e94560; color: white; border: none; padding: 10px 20px; cursor: pointer; font-size: 16px; border-radius: 5px; }
        button:hover { background: #c23050; }
        .flag { background: #0f3460; padding: 20px; margin-top: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1> Cookie Monster's Vault</h1>
        <p>Welcome, <strong>{{ role }}</strong>!</p>
        {% if role == 'admin' %}
            <div class="flag">
                <h2> Admin Access Granted!</h2>
                <p>Here's your flag:</p>
                <code>{{ flag }}</code>
            </div>
        {% else %}
            <p>Only admins can access the vault.</p>
            <p>Your current role: <code>{{ role }}</code></p>
        {% endif %}
        <form method="POST" action="/reset">
            <button type="submit">Reset Session</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    role = request.cookies.get('role', 'guest')
    flag = FLAG if role == 'admin' else 'Access Denied'
    return render_template_string(HOME_PAGE, role=role, flag=flag)

@app.route('/reset', methods=['POST'])
def reset():
    resp = make_response('Redirecting...')
    resp.set_cookie('role', 'guest')
    resp.headers['Location'] = '/'
    resp.status_code = 302
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)