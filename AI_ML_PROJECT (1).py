import json
import os

DATA_FILE = "expenses.json"

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    data = load_data()
    data.append(expense)
    save_data(data)

    print("✅ Expense added successfully!\n")

# View expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.\n")
        return

    print("\n📋 All Expenses:")
    for exp in data:
        print(f"{exp['date']} | ₹{exp['amount']} | {exp['category']}")
    print()

# Calculate summary
def calculate_summary():
    data = load_data()
    if not data:
        print("No data available.\n")
        return

    income = float(input("Enter your monthly income: ₹"))

    total_expense = sum(exp["amount"] for exp in data)
    savings = income - total_expense

    # Investment suggestion (50% of savings)
    investment = savings * 0.5 if savings > 0 else 0

    print("\n📊 Financial Summary:")
    print(f"Total Expenses: ₹{total_expense}")
    print(f"Savings: ₹{savings}")

    if savings > 0:
        print(f"Suggested Investment: ₹{investment}")
    else:
        print("⚠️ You have exceeded your budget!")

    # Category-wise breakdown
    category_summary = {}
    for exp in data:
        category_summary[exp["category"]] = category_summary.get(exp["category"], 0) + exp["amount"]

    print("\n📂 Category-wise Spending:")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt}")

    print()

# Main menu
def main():
    while True:
        print("==== Smart Expense & Investment Planner ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Financial Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_summary()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
