from expense_functions import add_expense, view_expenses, total_expenses, filter_by_category, safe_to_file, load_from_file

# main function - controls the entire program
def main():
    expenses = load_from_file()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Categoy")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        # add expense - takes amount, category, and description
        if choice == "1":
            try:
                amount = float(input("Enter the amount number: "))
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                add_expense(expenses, amount, category, description)
                print("Expense added successfully")
            except ValueError:
                print("Invalid amount. Please enter valid number.")

        # view expenses - shows all saved expenses
        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        # total expenses - shows the total amount spent
        elif choice == "4":
            category = input("Enter category to filter: ")
            filter_by_category(expenses, category)
        # save and exit - saves expenses and ends the program
        elif choice == "5":
            safe_to_file(expenses)
            print("Expenses saved")
            break
        else:
            print("invalid choice. please try again.")

# run the program if this file is executed directly
if __name__ == "__main__":
    main()

