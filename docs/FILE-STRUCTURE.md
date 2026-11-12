# FIN basic file structure
 Three layers

| Layer | File | What belongs there |

| Frontend UI | `frontend/src/ui.py` | Starts the browser interface and handles screens and forms. |
| Application | `backend/src/application.py` | Handles sign-in, checks inputs, and applies FIN's business rules. |
| Database | `backend/src/db/database.py` | Defines the SQLite tables and handles reads and writes. |
## Project tree

cs370Project/
├── .gitignore
├── README.md
├── frontend/
│   ├── src/
│   │   ├── ui.py  (Frontend UI layer)
│   │   ├── api/
│   │   │   └── client.py
│   │   └── screens/
│   │       ├── accounts.py
│   │       ├── budgets.py
│   │       ├── goals.py
│   │       ├── knowledge.py
│   │       ├── layout.py
│   │       ├── styles.py
│   │       └── transactions.py
│   ├── styles/
│   └── tests/
│       └── test_browser.py
├── backend/
│   ├── src/
│   │   ├── application.py  (Application layer)
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── accounts.py
│   │   │   │   ├── budget_summary.py
│   │   │   │   ├── budgets.py
│   │   │   │   ├── goal_progress.py
│   │   │   │   ├── goals.py
│   │   │   │   ├── knowledge.py
│   │   │   │   └── transactions.py
│   │   │   ├── __init__.py
│   │   │   └── dependencies.py
│   │   ├── db/
│   │   │   ├── database.py  (Database layer)
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_users_and_transactions.py
│   │   │   │   ├── 0002_budgets.py
│   │   │   │   ├── 0003_goals.py
│   │   │   │   └── 0004_knowledge.py
│   │   │   ├── repositories/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── accounts.py
│   │   │   │   ├── budgets.py
│   │   │   │   ├── goals.py
│   │   │   │   ├── interfaces.py
│   │   │   │   ├── knowledge.py
│   │   │   │   └── transactions.py
│   │   │   └── __init__.py
│   │   ├── integrations/
│   │   │   ├── __init__.py
│   │   │   └── knowledge_provider.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── accounts.py
│   │   │   ├── budget_summary.py
│   │   │   ├── budgets.py
│   │   │   ├── goal_progress.py
│   │   │   ├── goals.py
│   │   │   ├── knowledge.py
│   │   │   └── transactions.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── accounts.py
│   │   │   ├── budget_summary.py
│   │   │   ├── budgets.py
│   │   │   ├── goal_progress.py
│   │   │   ├── goals.py
│   │   │   ├── knowledge.py
│   │   │   └── transactions.py
│   │   ├── __init__.py
│   │   └── config.py
│   ├── tests/
│   │   ├── integration/
│   │   │   ├── __init__.py
│   │   │   ├── test_app.py
│   │   │   └── test_release_flow.py
│   │   ├── unit/
│   │   │   ├── __init__.py
│   │   │   ├── test_accounts.py
│   │   │   ├── test_budget_summary.py
│   │   │   ├── test_budgets.py
│   │   │   ├── test_goal_progress.py
│   │   │   ├── test_goals.py
│   │   │   ├── test_knowledge.py
│   │   │   └── test_transactions.py
│   │   └── __init__.py
│   └── pyproject.toml
└── docs/
    ├── sprints/
    │   └── sprint-01.md
    ├── API-CONTRACT.md
    ├── FILE-STRUCTURE.md
    └── SPRINTS.md
```