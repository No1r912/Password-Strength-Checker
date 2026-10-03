import re


COMMON_PASSWORDS = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "letmein",
    "12345678"
]


def check_password(password):

    score = 0
    feedback = []


    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8-12 characters")


    # Uppercase
    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")


    # Lowercase
    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")


    # Numbers
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")


    # Symbols
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")


    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This password is commonly used")


    # Rating
    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"


    return score, strength, feedback