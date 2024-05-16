import re

def assess_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength = 0
    
    # Length
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if length >= 16:
        strength += 1
    
    # Presence of character types
    types_count = has_upper + has_lower + has_digit + has_special
    if types_count >= 3:
        strength += 1
    
    # Feedback
    if strength == 0:
        feedback = "Very Weak"
    elif strength == 1:
        feedback = "Weak"
    elif strength == 2:
        feedback = "Moderate"
    elif strength == 3:
        feedback = "Strong"
    else:
        feedback = "Very Strong"
    
    return feedback

# Example usage:
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password Strength:", strength)
