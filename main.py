from file_manager import load_expenses, save_expenses

from expense_manager import (
    add_expense,
    view_expenses,
    total_expenses,
    category_wise_expenses,
    search_by_category,
    delete_expense,
    monthly_budget_check
)


def show_menu():
    print("\n================================")
    print("       HOSTEL EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Category-wise Expenses")
    print("5. Search by Category")
    print("6. Delete Expense")
    print("7. Monthly Budget")
    print("8. Exit")


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_wise_expenses(expenses)

        elif choice == "5":
            search_by_category(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            monthly_budget_check(expenses)

        elif choice == "8":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
