from nicegui import ui

from backend.src.application import CATEGORIES, ExpenseTracker, category_totals

def format_dollars(cents):
    dollars, remainder = divmod(cents, 100)
    return f"${dollars:,}.{remainder:02d}"

@ui.page("/")
def expense_page():
    tracker = ExpenseTracker()

    ui.label("FIN Basuc Expense Demo").classes("text-2xl font-semibold")
    ui.label("Creates a simple expense list.")

    amount = ui.input("Amount (USD)", value="", placeholder="8.50")
    category = ui.select(list(CATEGORIES), label="Category", value="Food")
    error = ui.label("").classes("text-red-700")

    def add_expense():
        try:
            tracker.add_expense(amount.value, category.value)
        except ValueError as exc:
            error.set_text(str(exc))
            return

        error.set_text("")
        amount.set_value("")
        expenses, total_cents = tracker.summary()
        total.set_text(f"Total: {format_dollars(total_cents)}")
        category_summary.set_text(
            " | ".join(
                f"{category}: {format_dollars(cents)}"
                for category, cents in category_totals(expenses).items()
            )
        )

        expense_list.clear()
        with expense_list:
            for expense in expenses:
                ui.label(
                    f"{expense.category} — {format_dollars(expense.amount_cents)}"
                )

    ui.button("Add Expense", on_click=add_expense)
    total = ui.label("Total: $0.00").classes("text-xl font-semibold")
    category_summary = ui.label("")
    expense_list = ui.column()
    with expense_list:
        ui.label("No expenses yet")

if __name__ == "__main__":
    ui.run(host="127.0.0.1", port=8080, reload=False)