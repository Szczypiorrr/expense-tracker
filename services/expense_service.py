from database.db import Session
from models.expense import Expense

def create_expense(amount, description, date, user_id, category_id):
    """
    Creates a new expense and saves it to database.
    """
    
    session = Session()

    expense = Expense(amount = amount, description = description, date = date, user_id = user_id, category_id = category_id)

    session.add(expense)
    session.commit()

    session.close()
    
    return expense

def get_all_expenses():
    """
    Returns all expenses from database.
    """

    session = Session()

    expenses = session.query(Expense).all()

    session.close()

    return expenses

def get_expenses_by_category(category_id):
    """
    Returns all expenses filtered by category_id.
    Returns None if no expenses found.
    """

    session = Session()

    expenses = session.query(Expense).where(Expense.category_id == category_id).all()

    if not expenses:
        return None
    
    session.close()

    return expenses