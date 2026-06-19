import re
from datetime import datetime

def validate_menu_option(option):
    """
    Validates if menu option is within allowed range.
    """
    if not option:
        return False

    if option < 1 or option > 8:
        return False
    
    return True


USERNAME_PATTERN = r"^[A-Za-z0-9_]{3,30}$"

def validate_username(username):
    if not username:
        return False

    username = username.strip()

    if not re.match(USERNAME_PATTERN, username):
        return False
    
    return True

def validate_amount(amount):
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
    if not description:
        return False
    
    if len(description) > 200:
        return False
    
    return True

CATEGORY_PATTERN = r"^[A-Za-z0-9_-]{3,30}$"


def validate_category_name(category_name):
    if not category_name: 
        return False
    
    category_name = category_name.strip()

    if not re.match(CATEGORY_PATTERN, category_name):
        return False
    
    return True

def validate_date(date_str):
    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return None
    