# Injection Master - Writeup

## Challenge Overview

**Category:** Web  
**Difficulty:** Easy  
**Points:** 200

SecureBank claims their login portal is completely secure. The goal is to bypass authentication and gain administrator access to retrieve the flag from the database.

## Reconnaissance

### Step 1: Analyze the Login Page

Navigate to `http://localhost:8003`

**Observations:**
- Standard login form with username and password fields
- Test credentials provided: `guest / guest`
- Hint suggests the system can be tested
- No visible security mechanisms (CAPTCHA, rate limiting)

### Step 2: Test Normal Functionality

Login with test credentials:
- Username: `guest`
- Password: `guest`

**Result:**
- Login successful
- Role displayed: `guest`
- Message: "Regular users don't have access to sensitive data"
- No flag visible

**Conclusion:** The flag is only accessible to users with `administrator` role.

## Vulnerability Analysis

### Identifying SQL Injection

The application likely uses a SQL query similar to:
```sql
SELECT * FROM users WHERE username = 'INPUT' AND password = 'INPUT'
```

If the application uses **string concatenation** instead of **parameterized queries**, we can inject SQL code through the input fields.

### Testing for SQLi

**Test Payload:** Enter a single quote `'` in the username field

If the application is vulnerable, this will break the SQL syntax and might:
- Return an error message
- Behave differently than normal input
- Allow SQL injection

### Understanding the Exploit

Classic SQL injection authentication bypass works by:

1. **Closing the username string:** `admin'`
2. **Commenting out the password check:** `--`

The SQL query becomes:
```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'
```

Everything after `--` is treated as a comment, so the password check is ignored!

## Exploitation

### Method 1: Basic SQLi Bypass (Easiest)

**Step 1:** Navigate to the login page

**Step 2:** Enter the following credentials:
- Username: `admin' --`
- Password: `anything`

**Step 3:** Click Login

**Explanation:**
- `admin'` closes the username string and targets the admin user
- `--` comments out the rest of the SQL query
- The password check is completely bypassed

**Result:** Admin access granted! 🎉

### Method 2: Boolean-Based SQLi

Alternative payload:
- Username: `admin' OR '1'='1' --`
- Password: `test`

This makes the WHERE clause always true:
```sql
WHERE username = 'admin' OR '1'='1' --' AND password = 'test'
```

### Method 3: UNION-Based SQLi (Advanced)

For extracting data directly:
```sql
' UNION SELECT username, password, role FROM users WHERE role='administrator' --
```

## Flag
```
FLAG{1nj3ct10n_1s_th3_qu33n_0f_vuln5}
```

## Vulnerable Code Analysis

### The Problem:
```python
# VULNERABLE CODE - String concatenation
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
```

**Why this is dangerous:**
- User input is directly embedded into the SQL query
- No validation or sanitization
- Allows arbitrary SQL code execution
- Attacker controls the query logic

### The Fix:

**Option 1: Parameterized Queries (Recommended)**
```python
# SECURE CODE
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

**Benefits:**
- Database treats user input as data, not code
- SQL injection impossible
- Industry standard approach

**Option 2: ORM (Object-Relational Mapping)**
```python
# Using SQLAlchemy ORM
user = User.query.filter_by(username=username, password=password).first()
```

**Option 3: Input Validation (Defense in Depth)**
```python
import re

# Whitelist validation
if not re.match(r'^[a-zA-Z0-9_]+$', username):
    return "Invalid username format"
```

**Best Practice:** Use parameterized queries AND input validation together.

## Real-World Impact

### OWASP Classification:
- **A03:2021 - Injection**
- Ranked #3 in OWASP Top 10 Web Application Security Risks

### Historical Breaches:

**1. Heartland Payment Systems (2008)**
- 130 million credit card numbers stolen
- SQL injection was the entry point
- Cost: $140 million in damages

**2. Sony Pictures (2011)**
- 1 million user accounts compromised
- Simple SQL injection vulnerability
- Massive reputation damage

**3. TalkTalk (2015)**
- 157,000 customers' data stolen
- Basic SQL injection attack
- £77 million in costs and fines

### Common Targets:
- Login forms (authentication bypass)
- Search fields (data extraction)
- URL parameters (GET requests)
- Cookie values (session manipulation)
- HTTP headers (User-Agent, Referer)

## Detection and Prevention

### For Developers:

1. **Always use parameterized queries**
2. **Never concatenate user input into SQL**
3. **Use ORMs with built-in protection**
4. **Implement input validation**
5. **Apply principle of least privilege** (database permissions)
6. **Use Web Application Firewalls (WAF)**
7. **Regular security testing and code reviews**

### For Penetration Testers:

**Tools:**
- SQLMap (automated SQLi tool)
- Burp Suite (manual testing)
- OWASP ZAP (vulnerability scanner)

**Manual Testing Checklist:**
- Test all input fields with `'`, `"`, `;`
- Try comment syntax: `--`, `#`, `/* */`
- Test boolean logic: `OR 1=1`, `AND 1=2`
- Try UNION queries for data extraction
- Test time-based blind SQLi: `SLEEP(5)`
- Check error messages for database info

## Key Takeaways

1. **SQL Injection is still prevalent** - Despite being well-known for 20+ years, it remains a critical vulnerability

2. **Simple fixes exist** - Parameterized queries solve the problem completely

3. **Defense in depth** - Combine multiple security layers (parameterization + validation + WAF)

4. **Never trust user input** - ALL user-controlled data must be treated as potentially malicious

5. **Test your applications** - Regular security testing catches these issues before attackers do

## Additional Resources

- [OWASP SQL Injection Guide](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [SQLMap Documentation](https://sqlmap.org/)

---

**CVE Examples:**
- CVE-2023-12345 (example pattern)
- CWE-89: SQL Injection
- CAPEC-66: SQL Injection Attack Pattern