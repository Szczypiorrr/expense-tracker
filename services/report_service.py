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

    print(f"Total expenses: {total_expenses} PLN\n")

    print(f"Number of expenses: {len(expenses)}\n")

    avarge_expense = session.query(func.avg(Expense.amount)).scalar()

    print(f"Avarge expense amount: {avarge_expense}\n")

    most_expensive = session.query(Expense).order_by(Expense.amount).first()

    print(f"Most expensive expense:\n{most_expensive.description} - {most_expensive.amount} PLN")

    categories = session.query(Category).all()

    print(f"Expenses by category:\n")
    for category in categories:
        total = sum(expense.amount for expense in category.expenses)
        print(f"{category.name} - {total}")

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

        f.write("SUMMARY\n")

        total_expenses = session.query(func.sum(Expense.amount)).where(and_(Expense.user_id == user.id, Expense.date >= date, Expense.date <= now)).scalar()
        f.write(f"Total expenses: {total_expenses} PLN\n")