import re


def validate_username(username):
    errors = []
    if len(username) < 5:
        errors.append("At least 5 characters")
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        errors.append("User Name allows only alphanumeric characters and underscores")
    return errors

def validate_email(email):
    errors = []
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        errors.append("Invalid email format")
    return errors

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("At least one digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("At least one special character")
    return errors