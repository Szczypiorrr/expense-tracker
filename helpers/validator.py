import re
from datetime import datetime

def validate_menu_option(option):
    """
    Validates menu option range (1-8).
    """

    if not option:
        return False

    if option < 1 or option > 8:
        return False
    
    return True


USERNAME_PATTERN = r"^[A-Za-z0-9_]{3,30}$"

def validate_username(username):
    """
    Validates username format.
    """

    if not username:
        return False

    username = username.strip()

    if not re.match(USERNAME_PATTERN, username):
        return False
    
    return True

def validate_amount(amount):
    """
    Validates if amount is a positive number.
    """

    if not amount:
        return False
    
    try:
        amount = float(amount)
    except:
        return False

    if amount < 0:
        return False
    
    return True

def validate_description(description):
    """
    Validates expense description length.
    """

    if not description:
        return False
    
    if len(description) > 200:
        return False
    
    return True


CATEGORY_PATTERN = r"^[A-Za-z0-9_-]{3,30}$"

def validate_category_name(category_name):
    """
    Validates category name format.
    """

    if not category_name: 
        return False
    
    category_name = category_name.strip()

    if not re.match(CATEGORY_PATTERN, category_name):
        return False
    
    return True

def validate_date(date_str):
    """
    Validates and parses date string.
    Expected format: YYYY-MM-DD HH:MM
    """

    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return None
    