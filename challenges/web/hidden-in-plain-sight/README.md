# Hidden in Plain Sight

**Category:** Web Exploitation  
**Difficulty:** Easy  
**Points:** 50  

---

## Description

Welcome to your first challenge! Sometimes the most valuable information is hidden where you least expect it. Can you find the flag?

**Challenge URL:** `http://localhost:8001`

---

## Learning Objectives

- Understanding HTML structure
- Learning to view page source code
- Introduction to client-side information disclosure

---

## Setup Instructions

### Build the Docker image:
```bash
docker build -t cipherforge/hidden-in-plain-sight .
```

### Run the container:
```bash
docker run -d -p 8001:80 --name hidden-in-plain-sight cipherforge/hidden-in-plain-sight
```

### Access the challenge:
Open your browser and navigate to: `http://localhost:8001`

### Stop the container:
```bash
docker stop hidden-in-plain-sight
docker rm hidden-in-plain-sight
```

---

## Flag Format
```
CipherForge{v13w_s0urc3_1s_y0ur_fr13nd}
```

---

## Hints

1. The flag isn't visible on the page itself
2. Try looking "under the hood"
3. Right-click might help you out

---

## Tags

`html` `source-code` `beginner` `web` `client-side`