# FIN file structure and ownership

FIN uses a conventional Python web application layout. The installable Python package lives under `backend/src/fin`, tests are separate from source, and the browser has its own folder. FastAPI routers handle HTTP, services own business rules, and repository interfaces keep those rules separate from SQLite. This structure adapts the FIN view, controller, service and DAO design. [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) · [FastAPI router guide](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

| Folder | Responsibility | Language |
| --- | --- | --- |
| `backend/src/fin/api` | Routes, auth dependency and HTTP status handling | Python |
| `backend/src/fin/schemas` | Request and response fields | Python |
| `backend/src/fin/services` | Validation, business rules and workflows | Python |
| `backend/src/fin/repositories` | DAO interfaces and SQLite queries | Python and SQL |
| `backend/src/fin/db` | Connections, transactions and numbered migrations | Python and SQL |
| `backend/src/fin/integrations` | Optional external knowledge provider | Python |
| `backend/tests` | Unit tests with fakes and integration tests with temporary databases | Python |
| `frontend` | Browser markup, styles, screens, HTTP client and browser tests | HTML, CSS and JavaScript |
| `docs` | Work breakdown, file map and planned API contract | Markdown |

`D1`–`D4` identify the file owner. `S1`–`S5` identify when the file is first used or extended. For example, `D3 · S1, 2` means Developer 3 starts the file in Sprint 1 and extends it in Sprint 2. All entries below are real files with notes in their native comment syntax.

```text
FIN-Sprint-Planning/
├── backend/
│   ├── src/
│   │   └── fin/
│   │       ├── api/
│   │       │   ├── routes/
│   │       │   │   ├── __init__.py                               D4 · S1 · Router package marker
│   │       │   │   ├── accounts.py                               D2 · S1, 2 · Account and session endpoints
│   │       │   │   ├── budget_summary.py                         D3 · S3 · Monthly spending summary endpoint
│   │       │   │   ├── budgets.py                                D2 · S3 · Monthly budget endpoints
│   │       │   │   ├── goal_progress.py                          D3 · S4 · Goal contributions and progress endpoints
│   │       │   │   ├── goals.py                                  D2 · S4 · Savings goal endpoints
│   │       │   │   ├── knowledge.py                              D2 · S5 · Financial knowledge endpoints
│   │       │   │   └── transactions.py                           D3 · S1, 2 · Expense and transaction endpoints
│   │       │   ├── __init__.py                                   D4 · S1 · API package marker
│   │       │   └── dependencies.py                               D2 · S1 · Authenticated identity
│   │       ├── db/
│   │       │   ├── migrations/
│   │       │   │   ├── 0001_users_and_transactions.sql           D4 · S1 · Initial SQLite schema
│   │       │   │   ├── 0002_budgets.sql                          D4 · S3 · Monthly budget schema change
│   │       │   │   ├── 0003_goals.sql                            D4 · S4 · Goal and contribution schema change
│   │       │   │   └── 0004_knowledge.sql                        D4 · S5 · Knowledge catalogue schema change
│   │       │   ├── __init__.py                                   D4 · S1 · Database package marker
│   │       │   └── connection.py                                 D4 · S1–5 · SQLite connection and migration handling
│   │       ├── integrations/
│   │       │   ├── __init__.py                                   D2 · S5 · External integration package marker
│   │       │   └── knowledge_provider.py                         D2 · S5 · Optional knowledge provider adapter
│   │       ├── repositories/
│   │       │   ├── __init__.py                                   D4 · S1 · Data access package marker
│   │       │   ├── accounts.py                                   D4 · S1, 2 · SQLite user and Personal account storage
│   │       │   ├── budgets.py                                    D4 · S3 · SQLite budget and allocation storage
│   │       │   ├── goals.py                                      D4 · S4 · SQLite goal and contribution storage
│   │       │   ├── interfaces.py                                 D4 · S1–5 · Shared DAO contracts
│   │       │   ├── knowledge.py                                  D4 · S5 · SQLite knowledge catalogue storage
│   │       │   └── transactions.py                               D4 · S1–3 · SQLite transaction storage and aggregation
│   │       ├── schemas/
│   │       │   ├── __init__.py                                   D4 · S1 · API schema package marker
│   │       │   ├── accounts.py                                   D2 · S1, 2 · Account request and response shapes
│   │       │   ├── budget_summary.py                             D3 · S3 · Spending comparison response
│   │       │   ├── budgets.py                                    D2 · S3 · Budget and allocation shapes
│   │       │   ├── goal_progress.py                              D3 · S4 · Contribution and progress shapes
│   │       │   ├── goals.py                                      D2 · S4 · Savings goal shapes
│   │       │   ├── knowledge.py                                  D2 · S5 · Article and search shapes
│   │       │   └── transactions.py                               D3 · S1, 2 · Expense and transaction shapes
│   │       ├── services/
│   │       │   ├── __init__.py                                   D4 · S1 · Service package marker
│   │       │   ├── accounts.py                                   D2 · S1, 2 · Registration, authentication and profile rules
│   │       │   ├── budget_summary.py                             D3 · S3 · Spending versus budget rules
│   │       │   ├── budgets.py                                    D2 · S3 · Monthly budget rules
│   │       │   ├── goal_progress.py                              D3 · S4 · Manual savings contribution rules
│   │       │   ├── goals.py                                      D2 · S4 · Goal creation and retrieval rules
│   │       │   ├── knowledge.py                                  D2 · S5 · Article search and fallback rules
│   │       │   └── transactions.py                               D3 · S1, 2 · Money and transaction rules
│   │       ├── __init__.py                                       D4 · S1 · Python package marker
│   │       ├── config.py                                         D4 · S1, 5 · Local application settings
│   │       └── main.py                                           D4 · S1–5 · Application entry point
│   ├── tests/
│   │   ├── integration/
│   │   │   ├── __init__.py                                       D4 · S1 · Integration test package marker
│   │   │   ├── test_app.py                                       D4 · S1–5 · HTTP and database integration tests
│   │   │   └── test_release_flow.py                              D3 · S5 · Full project regression test
│   │   ├── unit/
│   │   │   ├── __init__.py                                       D4 · S1 · Unit test package marker
│   │   │   ├── test_accounts.py                                  D2 · S1, 2 · Account and session unit tests
│   │   │   ├── test_budget_summary.py                            D3 · S3 · Budget summary unit tests
│   │   │   ├── test_budgets.py                                   D2 · S3 · Budget unit tests
│   │   │   ├── test_goal_progress.py                             D3 · S4 · Goal contribution and progress unit tests
│   │   │   ├── test_goals.py                                     D2 · S4 · Goal unit tests
│   │   │   ├── test_knowledge.py                                 D2 · S5 · Financial knowledge unit tests
│   │   │   └── test_transactions.py                              D3 · S1, 2 · Transaction unit tests
│   │   └── __init__.py                                           D4 · S1 · Python test package marker
│   └── pyproject.toml                                            D4 · S1 · Python package and tools
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js                                         D1 · S1–5 · Browser HTTP adapter
│   │   ├── ui/
│   │   │   ├── accounts.js                                       D1 · S1, 2 · Registration, sign-in and profile UI
│   │   │   ├── budgets.js                                        D1 · S3 · Monthly budgets UI
│   │   │   ├── goals.js                                          D1 · S4 · Savings goals UI
│   │   │   ├── knowledge.js                                      D1 · S5 · Knowledge browser UI
│   │   │   └── transactions.js                                   D1 · S1, 2 · Expense and transaction UI
│   │   └── main.js                                               D1 · S1–5 · Browser startup and view coordination
│   ├── styles/
│   │   └── main.css                                              D1 · S1–5 · Browser styles
│   ├── tests/
│   │   └── browser.test.mjs                                      D1 · S1–5 · Browser behavior test notes
│   └── index.html                                                D1 · S1–5 · Browser entry page and screens
└── .gitignore                                                    D4 · S1 · Git exclusions
```

Read the [sprint checklist index](SPRINTS.md) for the ordered steps, handoffs and demo for each sprint.
