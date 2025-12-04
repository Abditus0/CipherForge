# Hidden in Plain Sight - Writeup

**Challenge:** Hidden in Plain Sight  
**Category:** Web Exploitation  
**Difficulty:** Easy  
**Points:** 50  

---

## Challenge Description

Players are presented with a simple web page that displays a welcome message and a hint. The flag is not visible on the page itself.

---

## Solution

### Step 1: Access the Challenge

Navigate to the challenge URL: `http://localhost:8001`

You'll see a purple gradient page with the title "Hidden in Plain Sight" and the text:
- "Welcome to your first challenge!"
- "The flag is closer than you think..."
- A hint: "Sometimes the most obvious places are the easiest to overlook."

### Step 2: Examine the Page

The hint suggests looking in "obvious places." In web challenges, this often means:
- Checking the HTML source code
- Looking at JavaScript files
- Examining network requests
- Checking cookies

### Step 3: View Page Source

**Method 1:** Right-click anywhere on the page → Select "View Page Source"

**Method 2:** Press `Ctrl + U` (Windows/Linux) or `Cmd + Option + U` (Mac)

**Method 3:** Press `F12` to open Developer Tools → Go to "Sources" or "Elements" tab

### Step 4: Find the Flag

Once viewing the source code, scroll through the HTML. You'll find an HTML comment near the bottom:
```html
<!-- TODO: Remove this before going to production! -->
<!-- FLAG: CipherForge{v13w_s0urc3_1s_y0ur_fr13nd} -->
<!-- Seriously, don't forget to remove this comment! -->
```

### Step 5: Submit the Flag

Copy the flag: `CipherForge{v13w_s0urc3_1s_y0ur_fr13nd}`

Submit it to CTFd to complete the challenge.

---

## Key Takeaway

This challenge demonstrates **client-side information disclosure** - a common security issue where sensitive information is included in HTML comments, JavaScript files, or other client-accessible resources.

In real-world scenarios, developers sometimes leave:
- API keys in JavaScript files
- Debugging comments with sensitive info
- Commented-out code revealing system architecture
- Database credentials in client-side code

**Best Practice:** Never include sensitive information in client-side code, even in comments.

---

## Tools Used

- Web Browser (any)
- Browser Developer Tools

---

## Difficulty Rating

⭐ Easy - Requires only basic web knowledge

**Skills Required:**
- Understanding that web pages have source code
- Ability to view HTML source
- Reading and understanding HTML comments

**Time to Solve:** 1-3 minutes for beginners