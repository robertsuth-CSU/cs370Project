# Sprint 1 — Accounts and first saved expense

**Goal.** A user registers, signs in, adds an expense and sees it after an app restart. A second user sees a separate list.

**Before starting.** Use the file structure and shared API contract to agree on fields and DAO inputs. The four developers can work in parallel using fake responses or repositories.

**Integration order.** Day 1 agree on fields and start the app shell. Day 2 build the four parts independently. Day 3 connect repositories and services. Day 4 connect the browser to the API. Day 5 run the two-user and restart demo.

[All sprints](../SPRINTS.md) · [File structure](../FILE-STRUCTURE.md) · [API contract](../API-CONTRACT.md)

## Developer 1 — Browser, forms and session UI

**Files.** [`frontend/index.html`](../../frontend/index.html), [`frontend/styles/main.css`](../../frontend/styles/main.css), [`frontend/src/main.js`](../../frontend/src/main.js), [`frontend/src/api/client.js`](../../frontend/src/api/client.js), [`frontend/src/ui/accounts.js`](../../frontend/src/ui/accounts.js), [`frontend/src/ui/transactions.js`](../../frontend/src/ui/transactions.js), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs)

- [ ] **S1-D1-01** Sketch the registration, sign-in and expense screens and their keyboard navigation.
- [ ] **S1-D1-02** Add labelled name, email and password fields, an expense form, a list and a total. Put error messages where a user can find and correct them.
- [ ] **S1-D1-03** Create a fake API client with success, loading and failure responses for the three screens.
- [ ] **S1-D1-04** Implement the real HTTP adapter and switch each form to it when the API is ready. Parse JSON errors and handle an empty 204 response.
- [ ] **S1-D1-05** Keep the session token in memory. Send it on protected requests, clear the private view on sign-out or 401, and show sign-in again.
- [ ] **S1-D1-06** Load saved expenses on sign-in. Add a valid expense, refresh the list from the server, and format cents for display.
- [ ] **S1-D1-07** Verify invalid input, duplicate clicks while saving, an empty list, a network error and a successful sign-out. Hand off the UI walkthrough to Developer 3 for review.

## Developer 2 — Registration, sign-in and authorization

**Files.** [`backend/src/fin/api/routes/accounts.py`](../../backend/src/fin/api/routes/accounts.py), [`backend/src/fin/api/dependencies.py`](../../backend/src/fin/api/dependencies.py), [`backend/src/fin/schemas/accounts.py`](../../backend/src/fin/schemas/accounts.py), [`backend/src/fin/services/accounts.py`](../../backend/src/fin/services/accounts.py), [`backend/tests/unit/test_accounts.py`](../../backend/tests/unit/test_accounts.py)

- [ ] **S1-D2-01** Agree with Developer 4 on the user repository interface and with Developer 1 on public user and session response fields.
- [ ] **S1-D2-02** Validate and normalize emails consistently. Agree on password length rules, coordinate an Argon2id dependency, and test the service against a fake repository.
- [ ] **S1-D2-03** Implement registration. Hash the password, call the atomic user-and-Personal-account write, and map a duplicate normalized email to 409.
- [ ] **S1-D2-04** Implement sign-in. Verify the stored hash, use a generic error for invalid credentials, and issue an opaque token with a one-hour expiry.
- [ ] **S1-D2-05** Implement the shared authentication dependency. Return the authenticated user for a current token and 401 for invalid, missing or expired credentials. Revoke the token on sign-out.
- [ ] **S1-D2-06** Wire the three account routes and check response status, public fields and the absence of password material in responses or logs.
- [ ] **S1-D2-07** Test successful registration and login, duplicate and invalid credentials, expiry and logout. Give Developer 3 the authenticated dependency and Developer 4 the feature review.

## Developer 3 — Expense rules and routes

**Files.** [`backend/src/fin/api/routes/transactions.py`](../../backend/src/fin/api/routes/transactions.py), [`backend/src/fin/schemas/transactions.py`](../../backend/src/fin/schemas/transactions.py), [`backend/src/fin/services/transactions.py`](../../backend/src/fin/services/transactions.py), [`backend/tests/unit/test_transactions.py`](../../backend/tests/unit/test_transactions.py)

- [ ] **S1-D3-01** Agree on request fields, category values, date format, ordering and expense response fields with Developers 1 and 4.
- [ ] **S1-D3-02** Define the expense request and response models. Accept decimal amount text and return exact integer cents.
- [ ] **S1-D3-03** Validate amount, category, date and optional description. Reject zero, negatives, more than two fractional digits and invalid calendar dates.
- [ ] **S1-D3-04** Use a fake repository to implement add and list. Pass the authenticated user ID explicitly to both repository methods.
- [ ] **S1-D3-05** Add the protected expense endpoints. Use an authentication override in tests until Developer 2's implementation is ready.
- [ ] **S1-D3-06** Test exact cent conversion, invalid fields, no-session requests and forwarding the correct owner. Verify empty and sorted lists.
- [ ] **S1-D3-07** Connect the routes to the real SQLite repository and review the UI's request and response handling with Developer 1.

## Developer 4 — Project setup, SQLite and integration

**Files.** [`.gitignore`](../../.gitignore), [`backend/pyproject.toml`](../../backend/pyproject.toml), [`backend/src/fin/config.py`](../../backend/src/fin/config.py), [`backend/src/fin/main.py`](../../backend/src/fin/main.py), [`backend/src/fin/db/connection.py`](../../backend/src/fin/db/connection.py), [`backend/src/fin/db/migrations/0001_users_and_transactions.sql`](../../backend/src/fin/db/migrations/0001_users_and_transactions.sql), [`backend/src/fin/repositories/interfaces.py`](../../backend/src/fin/repositories/interfaces.py), [`backend/src/fin/repositories/accounts.py`](../../backend/src/fin/repositories/accounts.py), [`backend/src/fin/repositories/transactions.py`](../../backend/src/fin/repositories/transactions.py), [`backend/tests/integration/test_app.py`](../../backend/tests/integration/test_app.py)

- [ ] **S1-D4-01** Set up the Python package, virtual environment, dependencies and Git exclusions. Document the clean setup and run commands once they work.
- [ ] **S1-D4-02** Agree on repository methods and an isolated test database path. Set up a testable app factory, health route and shared safe error responses.
- [ ] **S1-D4-03** Write the initial migration for users, Personal accounts and transactions. Add foreign keys, normalized email uniqueness and exact cent constraints.
- [ ] **S1-D4-04** Implement connections and numbered migrations. Enable foreign keys per connection and verify commit, rollback and repeat startup.
- [ ] **S1-D4-05** Implement the atomic user/account write, credential lookup and owner-scoped expense insert and list. Bind query parameters and verify date and ID ordering.
- [ ] **S1-D4-06** Register the routers, attach repositories to services and serve the frontend from the same local server. Integrate storage, accounts, expenses and browser in that order.
- [ ] **S1-D4-07** Test startup from a clean directory, rollback on a failed registration, two-user isolation and restart persistence. Have Developer 1 run the setup from a clean copy.

## Sprint demo

- [ ] Create two users. As the first, add a 12.50 expense and check 1,250 cents in the API. Show the second user's empty list. Restart, sign back in as the first user and verify the expense still appears. Sign out and confirm that the old token fails.
- [ ] Record the verification results and remaining work in the sprint review.
