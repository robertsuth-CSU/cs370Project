# Sprint 4 — Savings goals and progress

**Goal.** A user creates a savings goal and records manual contributions with persistent progress.

**Before starting.** Reuse authenticated identity, amount validation conventions and the migration runner from prior sprints. A contribution is a manual tracking entry.

**Integration order.** Agree on goal and contribution shapes. Build goal creation and progress independently. Integrate storage and verify progress at zero, below target and at or above target.

[All sprints](../SPRINTS.md) · [File structure](../FILE-STRUCTURE.md) · [API contract](../API-CONTRACT.md)

## Developer 1 — Goal forms, contributions and progress UI

**Files.** [`frontend/index.html`](../../frontend/index.html), [`frontend/styles/main.css`](../../frontend/styles/main.css), [`frontend/src/api/client.js`](../../frontend/src/api/client.js), [`frontend/src/ui/goals.js`](../../frontend/src/ui/goals.js), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs)

- [ ] **S4-D1-01** Add a goal creation form with name, target and deadline, and a list of owned goals.
- [ ] **S4-D1-02** Build a goal detail view with the deadline, saved amount, target and accessible progress indicator.
- [ ] **S4-D1-03** Add a contribution form with amount input and a pending state that prevents repeated clicks.
- [ ] **S4-D1-04** Connect goal and contribution calls. Refresh the goal after a successful contribution and display the server's calculated progress.
- [ ] **S4-D1-05** Handle invalid amounts, unavailable goals, expired sessions and server failures.
- [ ] **S4-D1-06** Verify keyboard navigation, zero progress, partial progress and completion in the real browser.

## Developer 2 — Goal creation, list and detail

**Files.** [`backend/src/fin/schemas/goals.py`](../../backend/src/fin/schemas/goals.py), [`backend/src/fin/services/goals.py`](../../backend/src/fin/services/goals.py), [`backend/src/fin/api/routes/goals.py`](../../backend/src/fin/api/routes/goals.py), [`backend/tests/unit/test_goals.py`](../../backend/tests/unit/test_goals.py)

- [ ] **S4-D2-01** Agree on required fields and deadline semantics. Share goal IDs and target amount fields with Developer 3.
- [ ] **S4-D2-02** Add request and response shapes for goal creation, list and details.
- [ ] **S4-D2-03** Validate the name, positive target and deadline. Convert target text to exact cents.
- [ ] **S4-D2-04** Implement create, list and detail through an owner-scoped goal repository with a fake for tests.
- [ ] **S4-D2-05** Expose the routes. Use consistent 404 responses for absent and unowned goal details.
- [ ] **S4-D2-06** Test valid creation, bad inputs, an empty list and another user's ID. Review the goal responses with Developer 1.

## Developer 3 — Contribution rules and progress API

**Files.** [`backend/src/fin/schemas/goal_progress.py`](../../backend/src/fin/schemas/goal_progress.py), [`backend/src/fin/services/goal_progress.py`](../../backend/src/fin/services/goal_progress.py), [`backend/src/fin/api/routes/goal_progress.py`](../../backend/src/fin/api/routes/goal_progress.py), [`backend/tests/unit/test_goal_progress.py`](../../backend/tests/unit/test_goal_progress.py)

- [ ] **S4-D3-01** Agree on the contribution contract and a retry policy with Developers 1 and 4.
- [ ] **S4-D3-02** Validate positive contribution amounts and send owner and goal IDs into an atomic repository operation.
- [ ] **S4-D3-03** Derive current savings from the recorded contributions. Preserve the full amount above target and cap only the displayed progress percentage.
- [ ] **S4-D3-04** Add contribution and progress endpoints. Use consistent missing/unowned errors and return the new progress on a successful save.
- [ ] **S4-D3-05** Test invalid amounts, empty and partial progress, exact completion and overfunding.
- [ ] **S4-D3-06** Verify concurrent contributions do not overwrite one another. Review the completed goal flow with Developers 1 and 2.

## Developer 4 — Goal and contribution storage

**Files.** [`backend/src/fin/db/migrations/0003_goals.sql`](../../backend/src/fin/db/migrations/0003_goals.sql), [`backend/src/fin/repositories/interfaces.py`](../../backend/src/fin/repositories/interfaces.py), [`backend/src/fin/repositories/goals.py`](../../backend/src/fin/repositories/goals.py), [`backend/src/fin/main.py`](../../backend/src/fin/main.py), [`backend/tests/integration/test_app.py`](../../backend/tests/integration/test_app.py)

- [ ] **S4-D4-01** Add the next migration for goals and contributions with required fields, positive integer cents, foreign keys and indexes.
- [ ] **S4-D4-02** Verify existing transactions and budgets survive the schema update.
- [ ] **S4-D4-03** Implement goal creation, list and detail scoped to the authenticated owner.
- [ ] **S4-D4-04** Implement an atomic contribution insert that checks the goal's owner as part of the write.
- [ ] **S4-D4-05** Read the goal and contribution total consistently. Wire the goal and progress routes to the real storage layer.
- [ ] **S4-D4-06** Test restart persistence, missing and unowned goals, and two contributions to the same goal. Confirm other users' savings do not affect totals.

## Sprint demo

- [ ] Create a 100.00 goal, contribute 25.00 and see 25% progress, then contribute 80.00 and see 105.00 saved and a complete state. Restart and verify the same amount. A second user cannot view or contribute to that goal.
- [ ] Record the verification results and remaining work in the sprint review.
