# Sprint 5 — Financial knowledge and final integration

**Goal.** A user can find and read educational articles. A teammate can install and demonstrate the complete local app from a clean copy.

**Before starting.** Use reviewed local articles as the baseline. At kickoff, decide whether an approved external knowledge provider is in scope and record its terms and expected response.

**Integration order.** Agree on article fields and local content. Build search and details, connect storage, then rehearse the full app with two users and a clean setup.

[All sprints](../SPRINTS.md) · [File structure](../FILE-STRUCTURE.md) · [API contract](../API-CONTRACT.md)

## Developer 1 — Knowledge search, details and browser demo

**Files.** [`frontend/index.html`](../../frontend/index.html), [`frontend/styles/main.css`](../../frontend/styles/main.css), [`frontend/src/api/client.js`](../../frontend/src/api/client.js), [`frontend/src/ui/knowledge.js`](../../frontend/src/ui/knowledge.js), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs)

- [ ] **S5-D1-01** Add a knowledge view with a labelled search field and a way to open article details.
- [ ] **S5-D1-02** Render titles, summaries, source names and safe source links. Treat provider content as text unless the team has approved a safe renderer.
- [ ] **S5-D1-03** Show loading, no results and catalogue unavailable states.
- [ ] **S5-D1-04** Connect search and detail requests. Discard a stale response when a newer search is already in progress.
- [ ] **S5-D1-05** Verify keyboard navigation and error states, including an unavailable provider.
- [ ] **S5-D1-06** Lead the final browser walkthrough from registration to knowledge search. Record any manual check still missing.

## Developer 2 — Knowledge service, routes and optional provider

**Files.** [`backend/src/fin/schemas/knowledge.py`](../../backend/src/fin/schemas/knowledge.py), [`backend/src/fin/services/knowledge.py`](../../backend/src/fin/services/knowledge.py), [`backend/src/fin/api/routes/knowledge.py`](../../backend/src/fin/api/routes/knowledge.py), [`backend/src/fin/integrations/knowledge_provider.py`](../../backend/src/fin/integrations/knowledge_provider.py), [`backend/tests/unit/test_knowledge.py`](../../backend/tests/unit/test_knowledge.py)

- [ ] **S5-D2-01** Agree on search limits, stable article IDs, source fields and the approved local articles.
- [ ] **S5-D2-02** Implement catalogue search and detail through the knowledge repository. Validate the query and result limits.
- [ ] **S5-D2-03** Add search and detail endpoints with predictable empty and missing-article responses.
- [ ] **S5-D2-04** If the team selects a provider, implement the server-side adapter with timeouts, response validation and local fallback.
- [ ] **S5-D2-05** Test empty queries or results, missing IDs, malformed provider data and timeouts with test doubles.
- [ ] **S5-D2-06** Review article attribution and verify the local catalogue works without provider settings.

## Developer 3 — Full application regression and release evidence

**Files.** [`backend/tests/integration/test_release_flow.py`](../../backend/tests/integration/test_release_flow.py), [`frontend/tests/browser.test.mjs`](../../frontend/tests/browser.test.mjs) (review with Developer 1), [`docs/sprints/sprint-05.md`](../../docs/sprints/sprint-05.md) (demo results)

- [ ] **S5-D3-01** Write the API walkthrough for two users, covering sign-in and owner isolation through the transaction, budget and goal flows.
- [ ] **S5-D3-02** Add exact-cent assertions, invalid requests and revoked-session coverage.
- [ ] **S5-D3-03** Recreate the app using the same database and verify the saved records and totals.
- [ ] **S5-D3-04** Test that knowledge search works without the provider and that earlier private data never appears in knowledge responses.
- [ ] **S5-D3-05** Pair with Developer 1 on the browser walkthrough and record the inputs, expected results and any differences.
- [ ] **S5-D3-06** Triage failures with the file owners and rerun the relevant checks after fixes. Record the outcome of each demo gate.

## Developer 4 — Catalogue data, startup and delivery

**Files.** [`backend/src/fin/db/migrations/0004_knowledge.sql`](../../backend/src/fin/db/migrations/0004_knowledge.sql), [`backend/src/fin/repositories/interfaces.py`](../../backend/src/fin/repositories/interfaces.py), [`backend/src/fin/repositories/knowledge.py`](../../backend/src/fin/repositories/knowledge.py), [`backend/src/fin/config.py`](../../backend/src/fin/config.py), [`backend/src/fin/main.py`](../../backend/src/fin/main.py), [`backend/tests/integration/test_app.py`](../../backend/tests/integration/test_app.py), [`README.md`](../../README.md)

- [ ] **S5-D4-01** Add the catalogue migration and a repeatable way to load reviewed articles with attribution.
- [ ] **S5-D4-02** Implement parameterized search and detail reads. Verify stable article IDs and result ordering.
- [ ] **S5-D4-03** Wire the knowledge routes and service. Read provider configuration only if the team selects an integration.
- [ ] **S5-D4-04** Rehearse startup from an empty database and upgrading an existing database through every numbered migration.
- [ ] **S5-D4-05** Document supported Python setup, install, startup, test, and demo commands in the README once verified.
- [ ] **S5-D4-06** Prepare a clean source handoff. Have a teammate follow the setup instructions and record the final integrated test results.

## Sprint demo

- [ ] From a clean setup, demonstrate accounts, transactions, budgets, savings goals and knowledge search. Stop and restart the app and check persistence. Verify the two-user privacy checks and that local articles still open with the external provider unavailable.
- [ ] Record the verification results and remaining work in the sprint review.
