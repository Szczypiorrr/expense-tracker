import calendar
from database.db import Session
from sqlalchemy import func, and_
from models.expense import Expense
from models.category import Category
from services.user_service import get_user
from datetime import datetime

def show_monthly_summary(month, year):
    session = Session()
    print("Monthly Summary\n")

    expenses = session.query(Expense).all()

    month_name = calendar.month_name[month]

    print(f"Month: {month_name} {year}\n")

    total_expenses = session.query(func.sum(Expense.amount)).scalar()

    print(f"Total expenses: {round(total_expenses, 2)} PLN\n")

    print(f"Number of expenses: {len(expenses)}\n")

    avarge_expense = session.query(func.avg(Expense.amount)).scalar()

    print(f"Avarge expense amount: {round(avarge_expense, 2)} PLN\n")

    most_expensive = session.query(Expense).order_by(Expense.amount).first()

    print(f"Most expensive expense:\n{most_expensive.description} - {most_expensive.amount} PLN")

    categories = session.query(Category).all()

    print(f"Expenses by category:\n")
    for category in categories:
        total = sum(expense.amount for expense in category.expenses)
        print(f"{category.name} - {round(total, 2)} PLN")

    session.close()




def generate_report(username, date):
    with open("reports/report.txt", "w") as f:
        session = Session()
        f.write("================= EXPENSE REPORT =================\n")

        user = get_user(username)
        f.write(f"User: {user.username}\n")

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        f.write("Period:\n")
        f.write(f"From: {date}\n")
        f.write(f"To: {now}\n\n")

        f.write("------------------------------------\n\n")

        expenses = session.query(Expense).where(and_(Expense.user_id == user.id, Expense.date >= date, Expense.date <= now)).all()

        f.write("SUMMARY:\n")

        total_expenses = session.query(func.sum(Expense.amount)).where(and_(Expense.user_id == user.id, Expense.date >= date, Expense.date <= now)).scalar()

        f.write(f"Total expenses: {round(total_expenses, 2)} PLN\n")
        f.write(f"Number of expenses: {len(expenses)}\n")

        avg_expenses = session.query(func.avg(Expense.amount)).where(and_(Expense.user_id == user.id, Expense.date >= date, Expense.date <= now)).scalar()

        f.write(f"Avarge expense: {round(avg_expenses, 2)} PLN\n\n")

        highest_expense = session.query(Expense).where(Expense.user_id == user.id).order_by(Expense.amount.desc()).first()

        f.write("HIGHEST EXPENSE:\n")
        f.write(f"{highest_expense.description} - {round(highest_expense.amount, 2)} PLN ({highest_expense.category.name})\n\n")

        lowest_expense = session.query(Expense).where(Expense.user_id == user.id).order_by(Expense.amount).first()

        f.write("LOWEST EXPENSE:\n")
        f.write(f"{lowest_expense.description} - {round(lowest_expense.amount, 2)} PLN ({lowest_expense.category.name})\n\n")

        f.write("BY CATEGORY:\n")
        category_totals = {}

        for expense in expenses:
            category_name = expense.category.name

            if category_name not in category_totals:
                category_totals[category_name] = 0

            category_totals[category_name] += expense.amount

        for name, total in category_totals.items():
            f.write(f"{name} - {round(total, 2)} PLN\n")

        f.write("\nTOP 5 EXPENSES:\n")
        i = 1
        for expense in expenses:
            if i <= 5:
                f.write(f"{i}. {expense.description} - {expense.amount} PLN\n")
                i += 1
        
        session.close()

