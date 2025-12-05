# Cookie Monster 🍪

**Category:** Web  
**Difficulty:** Easy-Medium  
**Points:** 150

## Description

Cookie Monster guards his vault carefully... or does he? 

The vault only allows admin access, but something seems off about how it checks user roles. Can you find a way to convince the system you're an administrator?

**Challenge URL:** `http://localhost:8002`

## Learning Objectives

- Understanding HTTP cookies
- Cookie manipulation techniques
- Client-side security pitfalls
- Browser Developer Tools usage

## Vulnerability

This challenge demonstrates **insecure cookie handling**. The application stores user roles in an unencrypted, unsigned cookie that can be easily modified by the client. The server blindly trusts the cookie value without any validation or cryptographic verification.

## Setup Instructions

### Build the Docker image:
```bash
docker build -t cookie-monster .
```

### Run the container:
```bash
docker run -d -p 8002:5000 --name cookie-monster cookie-monster
```

### Access the challenge:
```
http://localhost:8002
```

### Stop the container:
```bash
docker stop cookie-monster
docker rm cookie-monster
```

## Flag Format

`FLAG{c00k13s_4r3_n0t_s3cur3_st0r4g3}`

## Hints

1. Check your browser's cookies - what do you see?
2. Cookies can be modified by the client
3. The server trusts whatever role you claim to be

## Files

- `app.py` - Flask web application with vulnerable cookie handling
- `flag.txt` - The flag file
- `Dockerfile` - Container configuration