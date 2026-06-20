# expense-tracker
A simple Expense Tracker CLI application built in Python using SQLAlchemy and a relational database.

The goal of this project is to demonstrate working with databases (SQLAlchemy ORM), data modeling, CRUD operations, reporting, input validation, CLI application design, and modular project architecture.

## ⚙️ How to run

### 1. Clone repository
```bash
git clone https://github.com/Szczypiorrr/expense-tracker.git
cd expense-tracker
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate virtual environment
Windows:
```bash
venv\Script\activate
```

Mac / Linux:
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Initialize database (optional)
Database is created automatically on first run.

### 6. Run project
```bash
python main.py
```

## 📌 Features

- Create users and categories
- Add expenses with amount, description and date
- Store all data in a relational database (SQLAlchemy ORM)
- View all expenses or filter by category
- Generate monthly expense summaries
- Generate detailed expense reports for a user and date range
- Calculate statistics (total, average, min, max expenses)
- Group expenses by category
- Top expenses listing
- Input validation for all user data
- Modular architecture (services, models, validation layer)
- CLI-based user interaction system

## 🧱 Project structure
```text
expense-tracker/
│
├── main.py # CLI application entry point
│
├── models/
│   ├── base_model.py # SQLAlchemy base declarative model
│   ├── expense.py # Expense model
│   ├── category.py # Category model
│   └── user.py # User model
│
├── services/
│   ├── user_service.py # User CRUD logic
│   ├── category_service.py # Category logic
│   ├── expense_service.py # Expense operations
│   └── report_service.py # Reports & analytics
│
├── database/
│   ├── db.py # SQLAlchemy session & engine
│   └── init_db.py # DB initialization
│
├── reports/
│   └── report.txt # Generated expense reports
│
├── helpers/
│   └── validator.py # Input validation layer
│
├── requirements.txt
│
└── README.md
```

## 🚀 Technologies

- Python 3.12
- Git/GitHub
- SQLAlchemy ORM
- SQLite (relational database)
- OOP
- CLI applications
- Data modeling & relationships
- File handling (report generation)

## 📊 Example CLI output
```text
====== WELCOME TO EXPENSE TRACKER ======

1. Create user
2. Add category
3. Add expense
4. Show all expenses
5. Show expenses by category
6. Show monthly summary
7. Generate report
8. Exit
```

## 📊 Example report output
```text
================= EXPENSE REPORT =================
User: test_user
Period:
From: 2026-01-01 00:00
To: 2026-01-20 14:30

SUMMARY:
Total expenses: 1200 PLN
Number of expenses: 15
Average expense: 80 PLN

HIGHEST EXPENSE:
Rent - 3000 PLN (Housing)

LOWEST EXPENSE:
Coffee - 5 PLN (Food)

BY CATEGORY:
Food - 300 PLN
Transport - 200 PLN
Housing - 700 PLN

TOP 5 EXPENSES:
1. Rent - 3000 PLN
2. Laptop - 2500 PLN
3. Groceries - 400 PLN
```

## 🧠 What I learned?

- Working with relational databases using SQLAlchemy ORM
- Designing data models and relationships
- CRUD operations in real applications
- Writing SQL-like queries in Python
- Building reporting systems (summary + analytics)
- Input validation and error handling
- CLI application design
- Structuring medium/large Python projects
- Applying DRY principle in practise

## 🔧 Possible improvements

- Add authentication system (login/password)
- Add budget limits per category
- Export reports to CSV or PDF
- Add recurring expenses system
- Add web version (FastAPI)
- Improve CLI UX (colors, tables, formatting)

# 👤 Author

Created by Szczypiorrrr  
🔗 GitHub: https://github.com/Szczypiorrr