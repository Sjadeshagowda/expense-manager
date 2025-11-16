import csv
from datetime import datetime

FILE = "expenses.csv"


# ---------------- Add Expense ----------------
def add_expense(amount, category):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), amount, category])
    print("✅ Expense added!")


# ---------------- View Expenses ----------------
def view_expenses():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            print("\nID | Date       | Amount | Category")
            print("-------------------------------------")
            for i, row in enumerate(reader, start=1):
                print(f"{i}  | {row[0]} | {row[1]} | {row[2]}")
    except FileNotFoundError:
        print("⚠️ No expenses found!")


# ---------------- Load all expenses ----------------
def load_expenses():
    try:
        with open(FILE, "r") as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []


# ---------------- Save all expenses ----------------
def save_expenses(expenses):
    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)


# ---------------- Edit Expense ----------------
def edit_expense():
    expenses = load_expenses()
    view_expenses()

    if not expenses:
        return

    exp_id = int(input("\nEnter expense ID to edit: "))

    if exp_id < 1 or exp_id > len(expenses):
        print("❌ Invalid ID!")
        return

    date, amount, category = expenses[exp_id - 1]

    print(f"\nEditing Expense {exp_id}:")
    print(f"Current Amount: {amount}")
    print(f"Current Category: {category}")

    new_amount = input("Enter new amount (press Enter to skip): ")
    new_category = input("Enter new category (press Enter to skip): ")

    if new_amount.strip():
        amount = new_amount
    if new_category.strip():
        category = new_category

    expenses[exp_id - 1] = [date, amount, category]
    save_expenses(expenses)

    print("✏️ Expense updated!")


# ---------------- Delete Expense ----------------
def delete_expense():
    expenses = load_expenses()
    view_expenses()

    if not expenses:
        return

    exp_id = int(input("\nEnter expense ID to delete: "))

    if exp_id < 1 or exp_id > len(expenses):
        print("❌ Invalid ID!")
        return

    expenses.pop(exp_id - 1)
    save_expenses(expenses)

    print("🗑️ Expense deleted!")


# ================= MAIN MENU =================
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        cat = input("Enter category: ")
        add_expense(amt, cat)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        edit_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")
