from database.db import Session
from models.expense import Expense

def create_expense(amount, description, date, user_id, category_id):
    session = Session()

    expense = Expense(amount = amount, description = description, date = date, user_id = user_id, category_id = category_id)

    session.add(expense)
    session.commit()

    session.close()
    
    return expense

def delete_expense(expense_id):
    session = Session()

    expense = session.query(Expense).where(Expense.id == expense_id).first()

    if not expense:
        session.close()
        return None

    session.delete(expense)
    session.commit()

    session.close()

    return

def get_expense(expense_id):
    session = Session()

    expense = session.query(Expense).where(Expense.id == expense_id).first()

    session.close()

    return expense

def get_all_expenses():
    session = Session()

    expenses = session.query(Expense).all()

    session.close()

    return expenses

def get_expenses_by_category(category_id):
    session = Session()

    expenses = session.query(Expense).where(Expense.category_id == category_id).all()

    if not expenses:
        return None
    
    session.close()

    return expenses