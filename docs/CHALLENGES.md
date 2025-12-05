# Challenge Index

Complete list of all CTF challenges in CipherForge.

---

## Web Exploitation

### 1. Hidden in Plain Sight
**Difficulty:** Easy  
**Points:** 50  
**Status:** ✅ Complete  

**Description:** Introduction to viewing HTML source code. Flag hidden in HTML comments.

**Skills Taught:**
- HTML source code inspection
- Client-side information disclosure
- Browser developer tools

**Files:** [`challenges/web/hidden-in-plain-sight/`](../challenges/web/hidden-in-plain-sight/)  
**Writeup:** [View Solution](../challenges/web/hidden-in-plain-sight/writeup.md)

---

### 2. Cookie Monster 🍪
- **Difficulty:** Easy-Medium
- **Points:** 150
- **Category:** Web
- **Concepts:** Cookie manipulation, client-side security, browser DevTools
- **Description:** Exploit insecure cookie handling to gain admin access
- **Files:** [Challenge Source](../challenges/web/cookie-monster/)
- **Writeup:** [Solution Guide](../challenges/web/cookie-monster/writeup.md)
- **Status:** ✅ Complete

**Learning Objectives:**
- Understanding HTTP cookies and their security implications
- Cookie manipulation techniques using browser Developer Tools
- Why client-side data should never be trusted
- Proper session management and authentication methods

**Screenshots:**
- [Landing Page](screenshots/cookie-monster/01-landing-page.png)
- [Guest Cookie](screenshots/cookie-monster/02-cookie-guest.png)
- [Admin Cookie](screenshots/cookie-monster/03-cookie-admin.png)
- [Flag Revealed](screenshots/cookie-monster/04-flag-revealed.png)

---

### 3. Injection Master 💉
- **Difficulty:** Medium
- **Points:** 200
- **Category:** Web
- **Concepts:** SQL Injection, database exploitation, authentication bypass
- **Description:** Exploit SQL injection to bypass login and gain administrator access
- **Files:** [Challenge Source](../challenges/web/injection-master/)
- **Writeup:** [Solution Guide](../challenges/web/injection-master/writeup.md)
- **Status:** ✅ Complete

**Learning Objectives:**
- Understanding SQL injection vulnerabilities and how they occur
- SQL query manipulation and comment-based bypass techniques
- Why parameterized queries are essential for security
- Real-world impact of SQLi attacks on authentication systems

**Screenshots:**
- [Login Page](screenshots/injection-master/01-login-page.png)
- [Guest Login](screenshots/injection-master/02-guest-login.png)
- [SQLi Payload](screenshots/injection-master/03-sqli-payload.png)
- [Flag Revealed](screenshots/injection-master/04-flag-revealed.png)