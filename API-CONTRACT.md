# Planned FIN API contract

Review these contracts at the start of the matching sprint. Routes use the authenticated user from a bearer token when reading or changing private records. Pass that identity through the service to the repository. The browser sends resource IDs and input fields, and the server derives the owner.

## Shared behavior

- Use same-origin requests from the browser. Keep an opaque session token in browser memory, require sign-in after expiry or restart, and revoke the token on sign-out.
- Send amounts as decimal text and return integer cents. Transactions and contributions require a positive amount. Budget allocations can be zero.
- Use `YYYY-MM-DD` for calendar dates and `YYYY-MM` for budget months. Sort transaction lists by newest date, then highest ID.
- Send safe error details. Use 401 for invalid credentials or a missing session, 404 for a missing or unowned resource, 409 for a duplicate account email, and 422 for rejected inputs. Keep credentials out of error bodies and logs.
- The success statuses below are targets for implementation. Treat 204 as an empty response in the browser client.

| Sprint | Planned endpoint | Input and result |
| --- | --- | --- |
| 1 | `GET /api/health` | 200 with a server status. |
| 1 | `POST /api/accounts` | Name, email and password. 201 with public user fields. |
| 1 | `POST /api/session` | Email and password. 200 with public user fields, access token and bearer token type. |
| 1 | `DELETE /api/session` | Revoke the presented token. 204. |
| 1 | `POST /api/expenses` | Amount text, category, date and optional description. 201 with the stored expense and amount in cents. |
| 1 | `GET /api/expenses` | 200 with the signed-in user's expenses, including an empty list. |
| 2 | `GET /api/profile` and `PATCH /api/profile` | Read the signed-in profile or change its display name. 200 with public fields. |
| 2 | `POST /api/transactions` | Kind, amount text, date, optional description, and expense category or income source. 201 with the stored record. |
| 2 | `GET /api/transactions` | Optional kind and inclusive start/end date filters. 200 with owned results. |
| 2 | `GET /api/transactions/{id}` and `PATCH /api/transactions/{id}` | Read or edit a record owned by the signed-in user. 200 with the record. |
| 2 | `DELETE /api/transactions/{id}` | Delete an owned record. 204. |
| 3 | `GET /api/budgets/{month}` and `PUT /api/budgets/{month}` | Read or replace that month's budget and category limits. 200 with the budget and allocations. A missing budget returns 404 on read. |
| 3 | `GET /api/budgets/{month}/summary` | 200 with category limits, expenses, remaining cents and overall totals. Include categories with expenses and zero allocation. |
| 4 | `POST /api/goals` and `GET /api/goals` | Create with name, target text and deadline, or list owned goals. 201 for create and 200 for list. |
| 4 | `GET /api/goals/{id}` | 200 with an owned goal's details. |
| 4 | `POST /api/goals/{id}/contributions` | Positive amount text. 201 with the recorded contribution and resulting progress. |
| 4 | `GET /api/goals/{id}/progress` | 200 with contributed cents, target cents, displayed percentage and completion. |
| 5 | `GET /api/knowledge` | Search terms and bounded result limits. 200 with article IDs, titles, summaries and sources. |
| 5 | `GET /api/knowledge/{id}` | 200 with article text and source attribution, or 404 when the article is unavailable. |

Developer 4 owns the repository interfaces. Developers 2 and 3 agree on methods and test against fakes before SQLite is integrated. Developer 1 uses the HTTP contract to build screens with mock responses.
