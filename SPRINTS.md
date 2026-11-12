# FIN sprint checklists

Replace Developer 1–4 with team names at kickoff. Use the [file structure](FILE-STRUCTURE.md) for ownership and the [API contract](API-CONTRACT.md) to coordinate between the browser, services and SQLite.

| Sprint | Goal |
| --- | --- |
| [Sprint 1 — Accounts and first saved expense](sprints/sprint-01.md) | A user registers, signs in, adds an expense and sees it after an app restart. A second user sees a separate list. |
| [Sprint 2 — Transaction management and profile](sprints/sprint-02.md) | A signed-in user records income, filters and manages their own transactions, and can update their display name. |
| [Sprint 3 — Monthly budgets and spending comparison](sprints/sprint-03.md) | A user sets category limits for a month and sees their actual expenses and remaining budget. |
| [Sprint 4 — Savings goals and progress](sprints/sprint-04.md) | A user creates a savings goal and records manual contributions with persistent progress. |
| [Sprint 5 — Financial knowledge and final integration](sprints/sprint-05.md) | A user can find and read educational articles. A teammate can install and demonstrate the complete local app from a clean copy. |

## Workstream owners

| Developer | Role across sprints | Review partner |
| --- | --- | --- |
| 1 | Browser UI, HTTP adapter and browser verification | Developer 3 |
| 2 | Accounts, authentication, and feature APIs for budgets, goals and knowledge | Developer 4 |
| 3 | Transactions, spending summaries, goal progress and final regression | Developer 2 |
| 4 | Python app setup, shared DAO contracts, SQLite and integration | Developer 1 |

## Use each checklist

1. Agree on the sprint goal and the shared inputs and outputs. Assign the four owners and choose the files for each branch.
2. Work in parallel with fake API responses or repositories while the real dependencies are being built. Update the agreed contract together if a change affects another owner.
3. Check off each task only after its expected behavior has been demonstrated or tested. Include the relevant task IDs and evidence in the review.
4. Integrate the completed parts and run the sprint demo. Carry forward incomplete work before starting a dependent sprint.

Suggested branch format is `sprint-01/d1-browser`, with corresponding names for the other owners and sprints. The branch names are labels for the team to use.

The file comments identify where to implement each part. The sprint checklists provide the order and acceptance criteria. Optional recurring entries and extra user roles are outside the five-sprint proposal until the team agrees on their behavior.
