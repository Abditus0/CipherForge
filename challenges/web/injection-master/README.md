# Injection Master 💉

**Category:** Web  
**Difficulty:** Medium  
**Points:** 200

## Description

Welcome to SecureBank's login portal! Our security team assures us that our authentication system is completely secure and immune to all attacks.

Can you prove them wrong and gain administrator access to retrieve the hidden flag?

**Challenge URL:** `http://localhost:8003`

## Learning Objectives

- Understanding SQL injection vulnerabilities
- How improper input validation leads to database compromise
- SQL query manipulation techniques
- The difference between secure and insecure database queries
- Why parameterized queries are essential

## Vulnerability

This challenge demonstrates **SQL Injection (SQLi)**, one of the most critical web vulnerabilities. The application constructs SQL queries using string concatenation instead of parameterized queries:
```python
# VULNERABLE CODE
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

This allows attackers to inject malicious SQL code through user inputs, bypassing authentication and accessing unauthorized data.

## Database Schema

### Users Table:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
```

**Test Credentials:**
- Admin: `admin / sup3r_s3cr3t_p@ssw0rd!` (you shouldn't need this!)
- Regular: `guest / guest`

### Flags Table:
```sql
CREATE TABLE flags (
    id INTEGER PRIMARY KEY,
    flag_text TEXT NOT NULL
)
```

## Setup Instructions

### Build the Docker image:
```bash
docker build -t injection-master .
```

### Run the container:
```bash
docker run -d -p 8003:5000 --name injection-master injection-master
```

### Access the challenge:
```
http://localhost:8003
```

### Stop the container:
```bash
docker stop injection-master
docker rm injection-master
```

## Flag Format

`FLAG{1nj3ct10n_1s_th3_qu33n_0f_vuln5}`

## Hints

1. The login form takes a username and password - what happens if you inject SQL syntax?
2. Try ending the SQL statement early with `--` (SQL comment)
3. Classic SQLi bypass: `' OR '1'='1`
4. You need administrator role to see the flag

## Files

- `app.py` - Flask application with vulnerable SQL query
- `init_db.py` - Database initialization script
- `flag.txt` - The flag file
- `Dockerfile` - Container configuration

## Real-World Impact

SQL Injection is listed as #3 in OWASP Top 10 (A03:2021 - Injection). Real attacks have:
- Compromised millions of user credentials
- Led to massive data breaches (Target, Sony, TalkTalk)
- Enabled privilege escalation and system takeover
- Cost companies billions in damages and fines