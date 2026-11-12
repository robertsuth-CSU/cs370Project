from dataclasses import dataclass, field
import math
import sqlite3
import tkinter as tk
from tkinter import ttk
from typing import Iterable, Union

BudgetInput = Union[tuple[str, float | int | str], list[tuple[str, float | int | str]]]


@dataclass
class BudgetResponse:
    """Standardized return object for FIN App operations."""
    success: bool
    message: str
    data: list[dict] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)


class FINDatabase:
    """Rightmost lifeline: manages SQLite persistence and duplicate checks."""

    def __init__(self, db_path: str = "fin_app.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    category_label TEXT NOT NULL COLLATE NOCASE,
                    limit_amount REAL NOT NULL CHECK(limit_amount > 0),
                    UNIQUE(user_id, category_label)
                )
                """
            )

    def check_for_duplicate_items(self, user_id: str, labels: Iterable[str]) -> bool:
        """Sequence step: 'Check for duplicates items' -> 'No duplicates found'."""
        cleaned = [label.strip().lower() for label in labels]
        if len(cleaned) != len(set(cleaned)):
            return True

        placeholders = ",".join("?" for _ in cleaned)
        query = f"""
            SELECT 1 FROM budgets
            WHERE user_id = ? AND LOWER(category_label) IN ({placeholders})
            LIMIT 1
        """
        cursor = self.conn.execute(query, [user_id, *cleaned])
        return cursor.fetchone() is not None

    def save_budget(self, user_id: str, items: list[tuple[str, float]]) -> bool:
        """Sequence step: 'Save Budget' -> 'Budget Saved'."""
        with self.conn:
            self.conn.executemany(
                """
                INSERT INTO budgets (user_id, category_label, limit_amount)
                VALUES (?, ?, ?)
                """,
                [(user_id, label, amount) for label, amount in items],
            )
        return True

    def get_all_budgets(self, user_id: str) -> list[dict]:
        cursor = self.conn.execute(
            """
            SELECT id, category_label, limit_amount
            FROM budgets
            WHERE user_id = ?
            ORDER BY id DESC
            """,
            (user_id,),
        )
        return [dict(row) for row in cursor.fetchall()]

    def clear_user_budgets(self, user_id: str) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM budgets WHERE user_id = ?", (user_id,))

    def close(self) -> None:
        self.conn.close()


class FINApp:
    """Middle lifeline: manages form display, input validation, and flow control."""

    def __init__(self, database: FINDatabase):
        self.db = database

    def select_create_budget(self) -> str:
        """Sequence step: 'Select Create Budget' -> 'Display Budget Form'."""
        return "Display Budget Form"

    def validate_input(
        self, items: BudgetInput
    ) -> tuple[bool, list[tuple[str, float]]]:
        """Self-call: 'Validate Input'."""
        raw_list = [items] if isinstance(items, tuple) else items
        if not isinstance(raw_list, list) or not raw_list:
            return False, []

        cleaned_items: list[tuple[str, float]] = []
        for entry in raw_list:
            if not isinstance(entry, (tuple, list)) or len(entry) != 2:
                return False, []

            label, amount = entry
            if not isinstance(label, str) or not (1 <= len(label.strip()) <= 50):
                return False, []

            if isinstance(amount, bool):
                return False, []

            try:
                numeric_amount = float(amount)
            except (TypeError, ValueError):
                return False, []

            if not math.isfinite(numeric_amount) or round(numeric_amount, 2) <= 0:
                return False, []

            cleaned_items.append((label.strip(), round(numeric_amount, 2)))

        return True, cleaned_items

    def enter_labels_and_amount(self, user_id: str, items: BudgetInput) -> BudgetResponse:
        """Sequence step: 'Enter labels and amount' -> Alternative [input is valid] / [Else]."""
        trace = [
            "Responsible Adult -> FIN App: Enter labels and amount",
            "FIN App -> FIN App: Validate Input",
        ]

        is_valid, cleaned_items = self.validate_input(items)

        if is_valid:
            trace.append("[Alternative: input is valid]")
            trace.append("FIN App -> Database: Check for duplicates items")
            labels = [label for label, _ in cleaned_items]
            has_duplicates = self.db.check_for_duplicate_items(user_id, labels)

            if not has_duplicates:
                trace.append("Database --> FIN App: No duplicates found")
                trace.append("FIN App -> Database: Save Budget")
                self.db.save_budget(user_id, cleaned_items)
                trace.append("Database --> FIN App: Budget Saved")
                trace.append("FIN App --> Responsible Adult: Budget Created Message")
                return BudgetResponse(
                    success=True,
                    message="Budget Created Message",
                    data=[
                        {"category": label, "limit": amount}
                        for label, amount in cleaned_items
                    ],
                    trace=trace,
                )
            else:
                trace.append("Database --> FIN App: Duplicate items detected!")

        trace.append("[Else]")
        trace.append(
            "FIN App --> Responsible Adult: Invalid input or duplicates found message"
        )
        return BudgetResponse(
            success=False,
            message="Invalid input or duplicates found message",
            trace=trace,
        )


class FINBudgetGUI:
    """Interactive Tkinter UI representing the 'Responsible Adult' actor."""

    def __init__(self, root: tk.Tk, app: FINApp, user_id: str = "responsible_adult_1"):
        self.root = root
        self.app = app
        self.user_id = user_id
        self.entry_rows: list[tuple[ttk.Entry, ttk.Entry, ttk.Frame]] = []

        self.root.title("FIN App - Create Budget (UML Sequence Tester)")
        self.root.geometry("720x640")
        self.root.minsize(680, 580)

        self._build_ui()
        self._refresh_budget_table()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Top Bar: Actor & Step 1 Button ("Select Create Budget")
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(
            top_frame,
            text="Actor: Responsible Adult",
            font=("Segoe UI", 11, "bold"),
        ).pack(side=tk.LEFT)

        self.start_btn = ttk.Button(
            top_frame,
            text="1. Select Create Budget",
            command=self.on_select_create_budget,
        )
        self.start_btn.pack(side=tk.RIGHT)

        # Step 2: Budget Form Frame (Initially locked until "Select Create Budget" is clicked)
        self.form_frame = ttk.LabelFrame(
            main_frame,
            text="Budget Form (Click '1. Select Create Budget' to activate)",
            padding=12,
        )
        self.form_frame.pack(fill=tk.X, pady=5)

        header_row = ttk.Frame(self.form_frame)
        header_row.pack(fill=tk.X, pady=(0, 4))
        ttk.Label(header_row, text="Category Label (e.g., Groceries)", width=35).pack(
            side=tk.LEFT, padx=(0, 10)
        )
        ttk.Label(header_row, text="Monthly Limit ($)", width=20).pack(side=tk.LEFT)

        self.rows_container = ttk.Frame(self.form_frame)
        self.rows_container.pack(fill=tk.X)

        self._add_input_row(enabled=False)

        # Form Action Buttons
        btn_row = ttk.Frame(self.form_frame)
        btn_row.pack(fill=tk.X, pady=(10, 0))

        self.add_row_btn = ttk.Button(
            btn_row,
            text="+ Add Another Category Row",
            command=lambda: self._add_input_row(enabled=True),
            state=tk.DISABLED,
        )
        self.add_row_btn.pack(side=tk.LEFT)

        self.submit_btn = ttk.Button(
            btn_row,
            text="2. Enter Labels and Amount (Submit)",
            command=self.on_submit_budget,
            state=tk.DISABLED,
        )
        self.submit_btn.pack(side=tk.RIGHT)

        # Status Banner for UML return messages
        self.status_label = tk.Label(
            main_frame,
            text="Waiting for 'Select Create Budget'...",
            font=("Segoe UI", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333",
            pady=8,
            relief=tk.GROOVE,
        )
        self.status_label.pack(fill=tk.X, pady=10)

        # Saved Budgets Table (View Budget Summary)
        table_frame = ttk.LabelFrame(
            main_frame, text="Saved Budgets in Database (fin_app.db)", padding=10
        )
        table_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        columns = ("id", "category", "limit")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=6
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("category", text="Category Label")
        self.tree.heading("limit", text="Budget Limit ($)")
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("category", width=320, anchor=tk.W)
        self.tree.column("limit", width=150, anchor=tk.E)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            table_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Reset DB Button for easy re-testing
        reset_btn = ttk.Button(
            main_frame,
            text="Clear Database Records (Reset Test)",
            command=self.on_clear_db,
        )
        reset_btn.pack(anchor=tk.E, pady=(2, 6))

        # Live Sequence Diagram Trace Log
        trace_frame = ttk.LabelFrame(
            main_frame, text="Live UML Sequence Diagram Trace", padding=8
        )
        trace_frame.pack(fill=tk.BOTH, expand=True)

        self.trace_text = tk.Text(
            trace_frame, height=6, font=("Consolas", 9), state=tk.DISABLED, bg="#1e1e1e", fg="#d4d4d4"
        )
        self.trace_text.pack(fill=tk.BOTH, expand=True)

    def _add_input_row(self, enabled: bool = True) -> None:
        row_frame = ttk.Frame(self.rows_container)
        row_frame.pack(fill=tk.X, pady=2)

        state = tk.NORMAL if enabled else tk.DISABLED
        label_entry = ttk.Entry(row_frame, width=38, state=state)
        label_entry.pack(side=tk.LEFT, padx=(0, 10))

        amount_entry = ttk.Entry(row_frame, width=22, state=state)
        amount_entry.pack(side=tk.LEFT, padx=(0, 10))

        if len(self.entry_rows) > 0:
            remove_btn = ttk.Button(
                row_frame,
                text="X",
                width=3,
                command=lambda rf=row_frame: self._remove_input_row(rf),
            )
            remove_btn.pack(side=tk.LEFT)

        self.entry_rows.append((label_entry, amount_entry, row_frame))

    def _remove_input_row(self, row_frame: ttk.Frame) -> None:
        self.entry_rows = [
            row for row in self.entry_rows if row[2] != row_frame
        ]
        row_frame.destroy()

    def _log_trace(self, lines: list[str]) -> None:
        self.trace_text.configure(state=tk.NORMAL)
        self.trace_text.delete("1.0", tk.END)
        for line in lines:
            self.trace_text.insert(tk.END, line + "\n")
        self.trace_text.configure(state=tk.DISABLED)

    def on_select_create_budget(self) -> None:
        """Step 1: Responsible Adult clicks 'Select Create Budget'."""
        form_response = self.app.select_create_budget()
        self.form_frame.configure(text=f"Budget Form ({form_response})")

        for label_entry, amount_entry, _ in self.entry_rows:
            label_entry.configure(state=tk.NORMAL)
            amount_entry.configure(state=tk.NORMAL)

        self.add_row_btn.configure(state=tk.NORMAL)
        self.submit_btn.configure(state=tk.NORMAL)
        self.entry_rows[0][0].focus_set()

        self.status_label.configure(
            text="Form Displayed: Enter category labels and dollar amounts below.",
            bg="#e6f2ff",
            fg="#004085",
        )
        self._log_trace(
            [
                "Responsible Adult -> FIN App: Select Create Budget",
                f"FIN App --> Responsible Adult: {form_response}",
            ]
        )

    def on_submit_budget(self) -> None:
        """Step 2: Responsible Adult submits 'Enter labels and amount'."""
        raw_items = [
            (label_entry.get(), amount_entry.get())
            for label_entry, amount_entry, _ in self.entry_rows
        ]

        response = self.app.enter_labels_and_amount(self.user_id, raw_items)
        self._log_trace(response.trace)

        if response.success:
            self.status_label.configure(
                text=f"SUCCESS: {response.message}",
                bg="#d4edda",
                fg="#155724",
            )
            # Clear input fields after successful creation
            for _, _, row_frame in self.entry_rows[1:]:
                row_frame.destroy()
            self.entry_rows = [self.entry_rows[0]]
            self.entry_rows[0][0].delete(0, tk.END)
            self.entry_rows[0][1].delete(0, tk.END)
            self._refresh_budget_table()
        else:
            self.status_label.configure(
                text=f"ERROR: {response.message}",
                bg="#f8d7da",
                fg="#721c24",
            )

    def _refresh_budget_table(self) -> None:
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.app.db.get_all_budgets(self.user_id):
            self.tree.insert(
                "",
                tk.END,
                values=(
                    item["id"],
                    item["category_label"],
                    f"${item['limit_amount']:,.2f}",
                ),
            )

    def on_clear_db(self) -> None:
        self.app.db.clear_user_budgets(self.user_id)
        self._refresh_budget_table()
        self.status_label.configure(
            text="Database cleared. Ready for new budget tests.",
            bg="#f0f0f0",
            fg="#333333",
        )


if __name__ == "__main__":
    db = FINDatabase("fin_app.db")
    fin_app = FINApp(db)

    root = tk.Tk()
    gui = FINBudgetGUI(root, fin_app)

    def on_closing() -> None:
        db.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()