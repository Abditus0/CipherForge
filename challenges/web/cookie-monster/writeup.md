# Cookie Monster - Writeup

## Challenge Overview

**Category:** Web  
**Difficulty:** Easy-Medium  
**Points:** 150

The challenge presents a web vault that only grants access to administrators. The goal is to bypass the role check and retrieve the flag.

## Reconnaissance

### Step 1: Visit the Website

Navigate to `http://localhost:8002`

**Observations:**
- Page displays: "Welcome, guest!"
- Message: "Only admins can access the vault"
- Shows current role as `guest`
- There's a "Reset Session" button

### Step 2: Inspect Network Traffic

Open Browser Developer Tools (`F12`) and check the **Application** or **Storage** tab.

**Finding:**
- A cookie named `role` exists
- Current value: `guest`
- The cookie is NOT encrypted or signed

## Vulnerability Analysis

The application suffers from **insecure direct object reference** via cookies:

1. User role is stored client-side in a plain text cookie
2. No cryptographic signature or validation
3. Server blindly trusts the cookie value
4. Anyone can modify their own cookies

**Code Snippet (vulnerable):**
```python
role = request.cookies.get('role', 'guest')
```

The server retrieves the role directly from the cookie without any verification.

## Exploitation

### Method 1: Browser Developer Tools (Easiest)

**Step 1:** Open Developer Tools (`F12`)

**Step 2:** Navigate to **Application** tab (Chrome) or **Storage** tab (Firefox)

**Step 3:** Find **Cookies** → `http://localhost:8002`

**Step 4:** Double-click the `role` cookie value

**Step 5:** Change `guest` to `admin`

**Step 6:** Refresh the page (`F5`)

**Result:** The flag appears!

### Method 2: Browser Console

Open Console tab in Developer Tools and run:
```javascript
document.cookie = "role=admin";
location.reload();
```

### Method 3: curl (Command Line)
```bash
curl -H "Cookie: role=admin" http://localhost:8002
```

## Flag
```
FLAG{c00k13s_4r3_n0t_s3cur3_st0r4g3}
```

## Remediation

### Vulnerable Code:
```python
role = request.cookies.get('role', 'guest')
if role == 'admin':
    return FLAG
```

### Secure Implementation:

**Option 1: Server-Side Sessions**
```python
from flask import session
# Store role in encrypted server-side session
session['role'] = 'guest'
```

**Option 2: Signed Cookies**
```python
from itsdangerous import URLSafeSerializer
s = URLSafeSerializer(secret_key)
# Sign the cookie value
signed_role = s.dumps({'role': 'guest'})
```

**Option 3: Proper Authentication**
- Use authentication tokens (JWT)
- Store user roles in a database
- Verify credentials on every request
- Never trust client-side data

## Key Takeaways

1. **Never trust client-side data** - Cookies, form inputs, and URLs can all be manipulated
2. **Use server-side sessions** - Store sensitive data on the server, not in cookies
3. **Sign your cookies** - If you must use cookies, use cryptographic signatures
4. **Implement proper authentication** - Use industry-standard methods like JWT or OAuth
5. **Validate everything** - Always verify user permissions on the server

## Real-World Impact

This vulnerability class has appeared in:
- E-commerce sites (price manipulation)
- Admin panels (privilege escalation)
- Banking apps (account number tampering)
- Gaming platforms (score manipulation)

**CVE Examples:**
- Similar issues classified under CWE-565 (Reliance on Cookies without Validation)
- OWASP Top 10: A01:2021 - Broken Access Control