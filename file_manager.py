import os
from config import FILE_NAME


def load_expenses():
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 4:
                amount, category, desc, date = parts

                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "desc": desc,
                    "date": date
                })

    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        for exp in expenses:
            line = (
                f"{exp['amount']},"
                f"{exp['category']},"
                f"{exp['desc']},"
                f"{exp['date']}\n"
            )

            file.write(line)
