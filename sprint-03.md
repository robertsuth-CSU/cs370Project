# Sprint 3 — Monthly budgets and spending comparison

**Goal.** A user sets category limits for a month and sees their actual expenses and remaining budget.

**Before starting.** Use Sprint 2's saved expenses and shared category names. This proposal uses one budget per user and calendar month.

**Integration order.** Agree on month and category rules. Build budget write/read and the summary separately. Add the migration and verify the combined comparison in the browser.

[All sprints](../SPRINTS.md) · [File structure](../FILE-STRUCTURE.md) · [API contract](../API-CONTRACT.md)

## Developer 1 — Budget editor and comparison view

**Files.** [`frontend/index.html`](../../frontend/index.html), [`frontend/styles/main.css`](../../frontend/styles/main.css), [`frontend/src/api/client.js`](../../frontend/src/api/client.js), [`frontend/src/ui/budgets.js`](../../frontend/src/ui/budgets.js), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs)

- [ ] **S3-D1-01** Add month selection and a budget editor with labelled category limits.
- [ ] **S3-D1-02** Load the selected month's saved limits and show an empty setup state when the user has no budget.
- [ ] **S3-D1-03** Submit limits as decimal text and show validation messages next to the affected inputs.
- [ ] **S3-D1-04** Display the summary returned by the API, including allocation, spent, remaining and unbudgeted expenses. Show negative remaining values clearly.
- [ ] **S3-D1-05** Refresh both the budget and summary on save. Handle a failed save and switching months without mixing responses.
- [ ] **S3-D1-06** Test empty, exact-limit and over-limit cases and verify the comparison against a saved expense in the real browser.

## Developer 2 — Budget model, service and API

**Files.** [`backend/src/fin/schemas/budgets.py`](../../backend/src/fin/schemas/budgets.py), [`backend/src/fin/services/budgets.py`](../../backend/src/fin/services/budgets.py), [`backend/src/fin/api/routes/budgets.py`](../../backend/src/fin/api/routes/budgets.py), [`backend/tests/unit/test_budgets.py`](../../backend/tests/unit/test_budgets.py)

- [ ] **S3-D2-01** Agree on month, budget name, category limits and missing-budget behavior with Developers 1, 3 and 4.
- [ ] **S3-D2-02** Validate calendar months, supported categories, nonnegative limits and unique categories.
- [ ] **S3-D2-03** Convert limits from decimal text to cents and define the owned budget and allocations response.
- [ ] **S3-D2-04** Implement read and atomic replacement through a fake repository first. Preserve the previous budget if any replacement row fails.
- [ ] **S3-D2-05** Add the budget read and replace endpoints. Share the agreed stored budget fields with Developer 3.
- [ ] **S3-D2-06** Test invalid month, duplicate categories, zero limit, exact cents, missing budget and replacement for the correct owner.

## Developer 3 — Monthly spending and remaining totals

**Files.** [`backend/src/fin/schemas/budget_summary.py`](../../backend/src/fin/schemas/budget_summary.py), [`backend/src/fin/services/budget_summary.py`](../../backend/src/fin/services/budget_summary.py), [`backend/src/fin/api/routes/budget_summary.py`](../../backend/src/fin/api/routes/budget_summary.py), [`backend/tests/unit/test_budget_summary.py`](../../backend/tests/unit/test_budget_summary.py)

- [ ] **S3-D3-01** Agree with Developer 4 on grouped expense totals by owner, category and date range.
- [ ] **S3-D3-02** Derive the month start and next month start. Include the first day and exclude the first day of the next month.
- [ ] **S3-D3-03** Combine category limits with the expense totals. Represent spending in unbudgeted categories as a zero limit.
- [ ] **S3-D3-04** Calculate per-category and overall remaining cents. Exclude income and retain negative values.
- [ ] **S3-D3-05** Add the signed-in summary endpoint and coordinate its response with Developer 1.
- [ ] **S3-D3-06** Test month boundaries, no budget, no expenses, unbudgeted categories, exact limit, overspending and owner scope.

## Developer 4 — Budget migration and owner-scoped storage

**Files.** [`backend/src/fin/db/migrations/0002_budgets.sql`](../../backend/src/fin/db/migrations/0002_budgets.sql), [`backend/src/fin/repositories/interfaces.py`](../../backend/src/fin/repositories/interfaces.py), [`backend/src/fin/repositories/budgets.py`](../../backend/src/fin/repositories/budgets.py), [`backend/src/fin/repositories/transactions.py`](../../backend/src/fin/repositories/transactions.py), [`backend/src/fin/main.py`](../../backend/src/fin/main.py), [`backend/tests/integration/test_app.py`](../../backend/tests/integration/test_app.py)

- [ ] **S3-D4-01** Add the next migration for budgets and allocations. Enforce one budget per owner and month and one limit per category.
- [ ] **S3-D4-02** Test the migration on a database containing Sprint 2 transactions and verify they are preserved.
- [ ] **S3-D4-03** Add owner/month repository reads and atomic replacement of budget rows and allocations.
- [ ] **S3-D4-04** Add a grouped expense query scoped to owner, category and the half-open month range. Use bound parameters.
- [ ] **S3-D4-05** Wire the budget and summary services and register their routers.
- [ ] **S3-D4-06** Test constraint failure and rollback, month changes, ownership and summary totals using SQLite. Give Developers 1–3 a shared demo dataset description.

## Sprint demo

- [ ] Set a 100.00 food limit, record 125.00 of food expenses and show −25.00 remaining. Add income, another user's expense and an expense outside the month. Verify none of those affect the comparison.
- [ ] Record the verification results and remaining work in the sprint review.
