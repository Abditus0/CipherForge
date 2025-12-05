# 🎯 CTF Challenges

This folder contains all custom-built CTF challenges for CipherForge.

## Completed Challenges

### Web Exploitation (3 challenges)

| # | Challenge Name | Difficulty | Points | Vulnerability Type |
|---|----------------|------------|--------|-------------------|
| 1 | Hidden in Plain Sight | Easy | 50 | HTML source code comments |
| 2 | Cookie Monster | Easy-Medium | 150 | Insecure Cookie Handling |
| 3 | Injection Master | Medium | 200 | SQL Injection |

---

### Standard Files:

- **Dockerfile** - Containerizes the challenge for consistent deployment
- **Challenge Files** - The vulnerable application or puzzle (app.py, index.html, etc.)
- **flag.txt** - Contains the flag in format `FLAG{...}`
- **README.md** - Challenge description, setup instructions, learning objectives
- **writeup.md** - Step-by-step solution with exploitation techniques

---

## Running Challenges Locally

Each challenge runs in its own Docker container:
```bash
# Navigate to challenge folder
cd challenges/web/challenge-name/

# Build the container
docker build -t challenge-name .

# Run the container (each uses different port)
docker run -d -p PORT:5000 --name challenge-name challenge-name

# Access at http://localhost:PORT
```

**Current Port Assignments:**
- Hidden in Plain Sight: `8001`
- Cookie Monster: `8002`
- Injection Master: `8003`

---
