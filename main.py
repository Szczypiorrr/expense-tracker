import time
from services.user_service import create_user, get_user
from services.category_service import create_category, get_category
from services.expense_service import create_expense, get_all_expenses, get_expenses_by_category
from database.init_db import init_database
from services.report_service import show_monthly_summary, generate_report
from helpers.validator import validate_menu_option, validate_username, validate_amount, validate_description, validate_category_name, validate_date

def message_and_return(message):
    """
    Simple helper function to show message and return to main menu after delay.
    """

    print(message)
    time.sleep(4)
    generate_menu()
    return 

def generate_menu():
    """
    Main CLI menu for Expense Tracker application.
    Handles user input and routes to proper functionality.
    """

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

    # ---------------- USER CREATION ----------------
    if option == 1:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        name = input("Enter username: ")
        
        if not validate_username(name):
            message_and_return("Username must consist of only A-Z, a-z, 0-9 and '_'")

        create_user(name)

        message_and_return("User created succesfully!")

    # ---------------- CATEGORY CREATION ----------------
    elif option == 2:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        category_name = input("Enter category name: ")

        if not validate_category_name(category_name):
            message_and_return("Category name must consist of only A-Z, a-z, 0-9, '_' and '-'")

        create_category(category_name)

        message_and_return("User created succesfully!")

    # ---------------- ADD EXPENSE ----------------
    elif option == 3:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        try:
            amount = float(input("Enter amount of this expense: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        if not validate_amount(amount):
            message_and_return("An error occured with amount.")

        description = input("Enter description of this expense: ")

        if not validate_description(description):
            message_and_return("Description must be a string and must have fewer than 200 characters.")

        date_str = input("Enter the date when this expense occurred (format RRRR-MM-DD HH:MM): ")

        date = validate_date(date_str)

        if not date:
            message_and_return("Invalid format, must be YYYY-MM-DD HH:MM.")

        user_name = input("Enter username: ")

        user = get_user(user_name)

        if not user:
            message_and_return("User not found")

        user_id = user.id
        
        category_name = input("Enter category name: ")

        if not validate_category_name(category_name):
            message_and_return("Category name must consist of only A-Z, a-z, 0-9, '_' and '-'")

        category_id = get_category(category_name).id

        if not category_id:
            message_and_return("Category not found")

        create_expense(amount, description, date, user_id, category_id)

        message_and_return("\nExpense created succesfully!")

    # ---------------- SHOW ALL EXPENSES ----------------
    elif option == 4:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        expenses = get_all_expenses()

        print("All expenses:")
        i = 1
        for expense in expenses:
            print(f"{i}. Expense ID: {expense.id} | Amount: {expense.amount} | Description: {expense.description} | Date: {expense.date} | User ID: {expense.user_id} | Category ID: {expense.category_id}")
            i += 1

        message_and_return("\nExpenses loaded succesfully!")

    # ---------------- FILTER BY CATEGORY ----------------
    elif option == 5:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        category_name = input("Enter category name: ")

        category_id = get_category(category_name).id

        if not category_id:
            message_and_return("User not found")

        expenses = get_expenses_by_category(category_id)

        if not expenses:
            message_and_return("No matches found.")

        message_and_return("\nExpenses by category loaded succesfully!")

    # ---------------- MONTHLY SUMMARY ----------------
    elif option == 6:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        try:
            month = int(input("Enter the number of month: "))
            year = int(input("Enter the number of year: "))
        except ValueError:
            message_and_return("Invalid type of data, must be a number.")
        except:
            message_and_return("An unexpected error occured.")

        show_monthly_summary(month, year)

        message_and_return("\nMonthly summary report generated succesfully!")

    # ---------------- REPORT GENERATION ----------------
    elif option == 7:
        if not validate_menu_option(option):
            message_and_return("Option must be a number between 1-8")

        name = input("Enter username: ")

        user = get_user(name)

        if not user:
            message_and_return("User not found")

        date_str = input("Enter the report start date (format RRRR-MM-DD HH:MM): ")

        date = validate_date(date_str)

        if not date:
            message_and_return("Invalid format, must be YYYY-MM-DD HH:MM.")

        generate_report(name, date)

        message_and_return("\nReport generated succesfully!")

    # ---------------- EXIT ----------------
    elif option == 8:
        print("Thank you for using our app, hope you enjoyed it!")
        time.sleep(4)
        return


if __name__ == "__main__":
    init_database()
    generate_menu()
