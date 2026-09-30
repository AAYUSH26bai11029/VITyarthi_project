from config import CATEGORIES


def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: ₹"))
    except ValueError:
        print("Please enter a valid number for amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    print("Categories:", ", ".join(CATEGORIES))
    category = input("Enter category: ").strip().title()

    if category not in CATEGORIES:
        print("Invalid category. Expense not added.")
        return

    desc = input("Enter short description: ").strip()
    date = input("Enter date (DD-MM-YYYY): ").strip()

    expenses.append({
        "amount": amount,
        "category": category,
        "desc": desc,
        "date": date
    })

    print("Expense added successfully!")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")

    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['desc']} | "
            f"{exp['date']}"
        )


def total_expenses(expenses):
    total = 0

    for exp in expenses:
        total += exp["amount"]

    print(f"Total expenses so far: ₹{total:.2f}")
    return total


def category_wise_expenses(expenses):
    totals = {}

    for exp in expenses:
        category = exp["category"]

        if category in totals:
            totals[category] += exp["amount"]
        else:
            totals[category] = exp["amount"]

    if len(totals) == 0:
        print("No expenses to show.")
        return

    print("\n--- Category-wise Spending ---")

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


def search_by_category(expenses):
    category = input(
        "Enter category to search: "
    ).strip().title()

    found = False

    print(f"\n--- {category} Expenses ---")

    for exp in expenses:
        if exp["category"] == category:
            print(
                f"₹{exp['amount']:.2f} | "
                f"{exp['desc']} | "
                f"{exp['date']}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")


def delete_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    try:
        number = int(
            input("Enter expense number to delete: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    removed = expenses.pop(number - 1)

    print(
        f"Deleted expense: {removed['desc']}"
    )


def monthly_budget_check(expenses):
    try:
        budget = float(
            input("Enter your monthly budget: ₹")
        )
    except ValueError:
        print("Invalid amount entered.")
        return

    if budget < 0:
        print("Budget cannot be negative.")
        return

    spent = total_expenses(expenses)
    remaining = budget - spent

    if remaining < 0:
        print(
            f"Warning! You have exceeded your "
            f"budget by ₹{-remaining:.2f}"
        )
    else:
        print(
            f"Remaining budget: ₹{remaining:.2f}"
        )
