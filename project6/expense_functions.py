import json
from datetime import datetime

# add a new expense
def add_expense(expenses, amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(expense)

# show all expenses
def view_expenses(expenses):
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['amount']} - {expense['category']} - {expense['description']} - {expense['date']} ")

# show total expenses
def total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")

# filter expenses by category
def filter_by_category(expenses, category):
    filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    for idx, expense in enumerate(filtered, start=1):
        print(f"{idx}. {expense['amount']} - {expense['description']} - {expense['date']}")

# save expenses to file
def safe_to_file(expenses, filename ="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# load expenses from file
def load_from_file(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    