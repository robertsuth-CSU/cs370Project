# Sprint 2 — Transaction management and profile

**Goal.** A signed-in user records income, filters and manages their own transactions, and can update their display name.

**Before starting.** Complete Sprint 1 first. Preserve the expense API and its saved records while adding a general transaction API.

**Integration order.** Agree on transaction kinds, filters and profile fields. Build the API and browser changes in parallel. Integrate writes and filters, then run migration-free restart and isolation checks.

[All sprints](../SPRINTS.md) · [File structure](../FILE-STRUCTURE.md) · [API contract](../API-CONTRACT.md)

## Developer 1 — Transaction list, editing and profile screens

**Files.** [`frontend/index.html`](../../frontend/index.html), [`frontend/styles/main.css`](../../frontend/styles/main.css), [`frontend/src/api/client.js`](../../frontend/src/api/client.js), [`frontend/src/ui/transactions.js`](../../frontend/src/ui/transactions.js), [`frontend/src/ui/accounts.js`](../../frontend/src/ui/accounts.js), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs)

- [ ] **S2-D1-01** Add controls to choose expense or income and show category or source as appropriate.
- [ ] **S2-D1-02** Add date and kind filters. Keep filter state clear and show empty results distinctly from failed requests.
- [ ] **S2-D1-03** Add a detail/edit form with saved values and a delete confirmation. Update the list only after a successful server response.
- [ ] **S2-D1-04** Add a profile panel that loads and edits the signed-in user's display name. Refresh the visible name after saving.
- [ ] **S2-D1-05** Connect the new API calls and handle invalid input, expired sessions and unavailable records.
- [ ] **S2-D1-06** Test the flows with fake responses. Then add income, edit an expense, delete a record and change the name in the real browser.

## Developer 2 — Profile API and session behavior

**Files.** [`backend/src/fin/api/routes/accounts.py`](../../backend/src/fin/api/routes/accounts.py), [`backend/src/fin/schemas/accounts.py`](../../backend/src/fin/schemas/accounts.py), [`backend/src/fin/services/accounts.py`](../../backend/src/fin/services/accounts.py), [`backend/tests/unit/test_accounts.py`](../../backend/tests/unit/test_accounts.py)

- [ ] **S2-D2-01** Agree on a narrow profile contract. Allow display-name edits and keep account identity fixed for this sprint.
- [ ] **S2-D2-02** Add public profile read and update models. Reject empty names and fields outside the agreed edit contract.
- [ ] **S2-D2-03** Add profile methods that derive the user ID from the authenticated session and call the owned repository record.
- [ ] **S2-D2-04** Add the read and update routes. Return the updated public profile without credential fields.
- [ ] **S2-D2-05** Test successful changes, invalid names, missing or expired sessions and attempted identity changes.
- [ ] **S2-D2-06** Give Developer 1 the profile responses and review the updated sign-in and sign-out regression tests.

## Developer 3 — Income, filters and transaction CRUD

**Files.** [`backend/src/fin/api/routes/transactions.py`](../../backend/src/fin/api/routes/transactions.py), [`backend/src/fin/schemas/transactions.py`](../../backend/src/fin/schemas/transactions.py), [`backend/src/fin/services/transactions.py`](../../backend/src/fin/services/transactions.py), [`backend/tests/unit/test_transactions.py`](../../backend/tests/unit/test_transactions.py)

- [ ] **S2-D3-01** Agree on the transaction kinds, filter bounds and partial update rules. Use inclusive dates and reject reversed date ranges.
- [ ] **S2-D3-02** Add income request validation with a source and expense validation with a category. Keep both amounts positive in storage and derive balance impact from kind.
- [ ] **S2-D3-03** Add list/filter and detail methods that call the repository with the authenticated owner and record ID.
- [ ] **S2-D3-04** Add edit and delete logic for owned records. Validate the resulting record after applying permitted changes.
- [ ] **S2-D3-05** Expose the general transaction routes and keep Sprint 1's expense route behavior. Use the same 404 for missing and unowned records.
- [ ] **S2-D3-06** Test income, expense, boundaries, partial edits, delete and cross-user access. Hand the confirmed contract to Developer 1.

## Developer 4 — Owned queries, profile writes and integration

**Files.** [`backend/src/fin/repositories/interfaces.py`](../../backend/src/fin/repositories/interfaces.py), [`backend/src/fin/repositories/accounts.py`](../../backend/src/fin/repositories/accounts.py), [`backend/src/fin/repositories/transactions.py`](../../backend/src/fin/repositories/transactions.py), [`backend/tests/integration/test_app.py`](../../backend/tests/integration/test_app.py)

- [ ] **S2-D4-01** Verify the Sprint 1 schema supports kind, category and source. Test upgrades from a saved Sprint 1 database before any schema change is approved.
- [ ] **S2-D4-02** Extend repository contracts with profile updates, filters, and owned record reads, edits and deletes.
- [ ] **S2-D4-03** Implement filter queries with bound parameters and deterministic date and ID ordering.
- [ ] **S2-D4-04** Implement owned writes with owner checks inside the update and delete queries. Report a missing row consistently.
- [ ] **S2-D4-05** Save profile changes only to the authenticated user and return the resulting public fields.
- [ ] **S2-D4-06** Test two users, date boundaries, existing expense compatibility and restart persistence. Review the integrated branch with Developers 1–3.

## Sprint demo

- [ ] Keep an expense from Sprint 1. Add income, filter by date and kind, edit an owned expense, delete an owned transaction and rename the profile. A second user cannot read, edit or delete the first user's transaction by ID.
- [ ] Record the verification results and remaining work in the sprint review.
