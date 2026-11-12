# Very basic database setup for an example 

from dataclasses import dataclass


@dataclass(frozen=True)
class Expense:
    category: str
    amount_cents: int

class ExpenseStore:
    def __init__(self):
        self._expenses = []

    def save(self, expense):
        self._expenses.append(expense)

    def list_expenses(self):
        return self._expenses.copy()