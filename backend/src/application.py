# basic expense tracker for demo

import re
from decimal import Decimal

from .db.database import Expense, ExpenseStore


CATEGORIES = ("Food", "Transport", "Bills", "Other")


class ExpenseTracker:
    def __init__(self):
        self._store = ExpenseStore()

    def add_expense(self, amount_text, category):
        amount_text = amount_text.strip()

        if not re.fullmatch(r"[0-9]{1,7}(?:\.[0-9]{1,2})?", amount_text):
            raise ValueError("Enter a positive amount with up to two decimal places.")

        amount_cents = int(Decimal(amount_text) * 100)
        if amount_cents == 0:
            raise ValueError("The amount must be greater than zero.")

        if category not in CATEGORIES:
            raise ValueError("Choose a category.")

        self._store.save(Expense(category, amount_cents))

    def summary(self):
        expenses = self._store.list_expenses()
        total_cents = sum(expense.amount_cents for expense in expenses)
        return expenses, total_cents

def category_totals(expenses):
    totals = {}
    for expense in expenses:
        totals[expense.category] = (
            totals.get(expense.category, 0) + expense.amount_cents
        )
    return totals