import json
from datetime import datetime

def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    
    expense = {
        "date": date,
        "amount": amount,
        "description": description,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully!")
    
def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def view_summaries(expenses):
    monthly_expenses = {}
    category_expenses = {}
    
    for expense in expenses:
        date = datetime.strptime(expense["date"], "%Y-%m-%d")
        month = date.strftime("%Y-%m")
        category = expense["category"]
        
        if month not in monthly_expenses:
            monthly_expenses[month] = 0
        monthly_expenses[month] += expense["amount"]
        
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += expense["amount"]
    
    print("Monthly Expenses:")
    for month, total in monthly_expenses.items():
        print(f"{month}: Rs.{total:.2f}")
    
    print("\nCategory-wise Expenses:")
    for category, total in category_expenses.items():
        print(f"{category}: Rs.{total:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summaries")
        print("3. Save Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summaries(expenses)
        elif choice == '3':
            save_expenses(expenses)
        elif choice == '4':
            save_expenses(expenses)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()