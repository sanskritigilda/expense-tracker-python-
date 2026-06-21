import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    expense_id = len(expenses) + 1

    print("\n===== Categories =====")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Bills")
    print("5. Entertainment")
    print("6. Health")
    print("7. Other")

    category_choice = input("Select category number: ")

    # Category selection using if-elif-else
    if category_choice == "1":
        category = "Food"
    elif category_choice == "2":
        category = "Travel"
    elif category_choice == "3":
        category = "Shopping"
    elif category_choice == "4":
        category = "Bills"
    elif category_choice == "5":
        category = "Entertainment"
    elif category_choice == "6":
        category = "Health"
    elif category_choice == "7":
        category = "Other"
    else:
        category = "Other"

    print(f"Selected Category: {category}")

    date = input("Enter date (DD-MM-YYYY): ")

    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))

    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("\nExpense Added Successfully!")
    print(f"Description : {description}")
    print(f"Amount      : ₹{amount:.2f}")
    print(f"Category    : {category}")
    print(f"Date        : {date}")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== All Expenses =====")
    print(f"Total Expenses: {len(expenses)}")

    for expense in expenses:
        print("-" * 40)
        print(f"ID          : {expense['id']}")
        print(f"Description : {expense['description']}")
        print(f"Amount      : ₹{expense['amount']:.2f}")
        print(f"Category    : {expense['category']}")
        print(f"Date        : {expense['date']}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    expense_id = int(input("Enter Expense ID to delete: "))

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return

    print("Expense ID not found.")


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spending: ₹{total:.2f}")


def view_categories():
    print("\n===== Categories =====")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Bills")
    print("5. Entertainment")
    print("6. Health")
    print("7. Other")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total Spending")
        print("5. View Categories")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # Switch Case (match-case)
        match choice:
            case "1":
                add_expense(expenses)

            case "2":
                view_expenses(expenses)

            case "3":
                delete_expense(expenses)

            case "4":
                calculate_total(expenses)

            case "5":
                view_categories()

            case "6":
                save_expenses(expenses)
                print("Data saved successfully!")

            case "7":
                save_expenses(expenses)
                print("Data saved. Exiting program...")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
