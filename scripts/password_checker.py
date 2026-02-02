#!/usr/bin/env python3
"""
Simple Password Strength Checker
Check if your password is strong enough!
"""

import getpass
import re


def check_password_strength(password):
    """
    Check how strong your password is
    Returns score and list of messages
    """
    score = 0
    messages = []
    
    # 1. Check Length
    if len(password) < 8:
        messages.append(" Too short! Use at least 8 characters")
    elif len(password) < 12:
        score += 1
        messages.append(" Length is OK, but 12+ is better")
    else:
        score += 2
        messages.append(" Great length!")
    
    # 2. Check for Uppercase Letters (A-Z)
    if re.search(r'[A-Z]', password):
        score += 1
        messages.append("Has uppercase letters")
    else:
        messages.append("Add uppercase letters (A-Z)")
    
    # 3. Check for Lowercase Letters (a-z)
    if re.search(r'[a-z]', password):
        score += 1
        messages.append("Has lowercase letters")
    else:
        messages.append(" Add lowercase letters (a-z)")
    
    # 4. Check for Numbers (0-9)
    if re.search(r'[0-9]', password):
        score += 1
        messages.append("Has numbers")
    else:
        messages.append("Add numbers (0-9)")
    
    # 5. Check for Special Characters (!@#$%^&*)
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?/\\|`~]', password):
        score += 1
        messages.append("Has special characters")
    else:
        messages.append("Add special characters (!@#$%)")
    
    # 6. Check for Common Weak Passwords
    weak_passwords = [
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'password123', '111111', 'welcome', 'admin', 'letmein'
    ]
    if password.lower() in weak_passwords:
        score = 0
        messages.append("This is a VERY common password! Change it!")
    
    return score, messages


def get_strength_level(score):
    """
    Convert score to strength rating
    """
    if score <= 2:
        return "WEAK ", "Your password can be cracked easily!"
    elif score <= 4:
        return "MEDIUM ", "Your password is OK but could be better"
    else:
        return "STRONG ", "Great! Your password is strong!"


def print_header():
    """Print a nice header"""
    print("\n" + "="*50)
    print("        PASSWORD STRENGTH CHECKER ")
    print("="*50)


def print_results(password, score, messages, strength, advice):
    """Print the results nicely"""
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)
    print(f"\nPassword Length: {len(password)} characters")
    print(f"Strength: {strength}")
    print(f"Score: {score}/7")
    print(f"\n{advice}")
    print("\n" + "-"*50)
    print("Details:")
    print("-"*50)
    for msg in messages:
        print(f"  {msg}")
    print("="*50)


def print_tips():
    """Print helpful tips"""
    print("\n" + "="*50)
    print(" TIPS FOR A STRONG PASSWORD")
    print("="*50)
    print("  1. Use at least 12 characters")
    print("  2. Mix uppercase AND lowercase letters")
    print("  3. Add numbers (0-9)")
    print("  4. Include special characters (!@#$%)")
    print("  5. Avoid common words like 'password' or '123456'")
    print("  6. Don't use personal info (name, birthday)")
    print("  7. Make each password unique")
    print("  8. Use a password manager to remember them")
    print("="*50 + "\n")


def main():
    """Main program"""
    # Show header
    print_header()
    
    # Show tips first
    print_tips()
    
    # Get password from user (hidden input for security)
    print("Enter your password to check its strength")
    print("(Don't worry - it won't be saved or shared!)\n")
    
    password = getpass.getpass("Password: ")
    
    # Check if password is empty
    if not password:
        print("\n Error: Please enter a password!\n")
        return
    
    # Check the password
    score, messages = check_password_strength(password)
    strength, advice = get_strength_level(score)
    
    # Show results
    print_results(password, score, messages, strength, advice)
    
    # Ask if user wants to try another password
    print("\n")
    again = input("Want to check another password? (y/n): ")
    if again.lower() == 'y':
        main()
    else:
        print("\nStay safe! Use strong passwords!\n")


# Run the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!\n")


