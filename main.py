import time
from services.user_service import create_user
from services.category_service import create_category
from datetime import datetime
from services.expense_service import create_expense, get_all_expenses, get_expenses_by_category
from database.init_db import init_database
from services.report_service import show_monthly_summary, generate_report

def message_and_return(message):
    print(message)
    time.sleep(4)
    return generate_menu()

def generate_menu():
    print("====== WELCOME TO EXPENSE TRACKER ======")
    print("1. Create user")
    print("2. Add category")
    print("3. Add expense")
    print("4. Show all expenses")
    print("5. Show expenses by category")
    print("6. Show monthly summary")
    print("7. Generate report")
    print("8. Exit")
    
    try:
        option = int(input("Enter seleted number: "))
    except ValueError:
        message_and_return("Invalid type of data, must be a number.")
    except:
        message_and_return("An unexpected error occured.")

    if option == 1:
        name = input("Enter username: ")
        
        if not name:
            message_and_return("An error occurred while enetring user name.")

        create_user(name)

        message_and_return("User created succesfully!")

    if option == 2:
        name = input("Enter category name: ")

        if not name:
            message_and_return("An error occurred while enetring category name.")

        create_category(name)

        message_and_return("User created succesfully!")

    if option == 3:
        try:
            amount = int(input("Enter amount of this expense: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        description = input("Enter description of this expense: ")

        date_str = input("Enter the date when this expense occurred (format RRRR-MM-DD HH:MM): ")

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except:
            message_and_return("Invalid format, must be RRRR-MM-DD HH:MM.")

        try:
            user_id = int(input("Enter user ID for this expense: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        try:
            category_id = int(input("Enter category ID for this expense: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        create_expense(amount, description, date, user_id, category_id)

        message_and_return("Expense created succesfully!")

    if option == 4:
        expenses = get_all_expenses()

        print("All expenses:")
        i = 1
        for expense in expenses:
            print(f"{i}. Expense ID: {expense.id} | Amount: {expense.amount} | Description: {expense.description} | Date: {expense.date} | User ID: {expense.user_id} | Category ID: {expense.category_id}\n")
            i += 1

        message_and_return("Expenses loaded succesfully!")

    if option == 5:
        try:
            category_id = int(input("Enter category ID: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        expenses = get_expenses_by_category(category_id)

        if not expense:
            message_and_return("No matches found.")

        message_and_return("Expenses by category loaded succesfully!")

    if option == 6:
        try:
            month = int(input("Enter the number of month: "))
            year = int(input("Enter the number of year: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        show_monthly_summary(month, year)

        message_and_return("\nMonthly summary report generated succesfully!")

    if option == 7:
        try:
            user_id = int(input("Enter user ID: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")


        date_str = input("Enter the report start date (format RRRR-MM-DD HH:MM): ")

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except:
            message_and_return("Invalid format, must be RRRR-MM-DD HH:MM.")

        generate_report(user_id, date)


if __name__ == "__main__":
    init_database()
    generate_menu()
