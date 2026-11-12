## Sprint 1

**Get one expense all the way from the browser into the database.** A new user should be able to register, sign in, add an expense, and find it again after restarting FIN.

### Developer A — Build the account and expense screens

Start in `frontend/index.html`, `frontend/src/ui/accounts.js`, and `frontend/src/ui/transactions.js`.

1. [ ] Make a registration form with name, email, and password. Make a sign-in form with email and password.
2. [ ] Make an expense form with amount, category, date, and optional description. Add a place to show saved expenses and their total.
3. [ ] Use made-up replies to check what the user sees while a form is saving, after success, and after an error.
4. [ ] Connect the forms to Python through `frontend/src/api/client.js`. Use the sign-in token, which is the temporary proof that the user signed in, for expense requests.
5. [ ] Load the user's expenses after sign-in and refresh the list after a successful save. Clear the screen and return to sign-in when the user signs out or the session expires.
6. [ ] Try an empty form, an invalid amount, and a valid **$12.50** expense. Check that a failed save leaves the list and total as they were.

**Done when** you can register and sign in through the browser, save $12.50, see it in the list and total, and sign out. Show Developer 3 the browser flow.

### Developer B — Make registration and sign-in work

Start in `backend/src/fin/services/accounts.py` and `backend/src/fin/api/routes/accounts.py`.

1. [ ] Agree with Developer 4 on the fields needed to save a user and look up their email.
2. [ ] Check the name, email, and password. Use the same email cleanup for registration and sign-in so a change in capitalization cannot create a second account.
3. [ ] Turn the password into a protected hash using the agreed password library. Ask Developer 4's save function to create the user and their Personal account together.
4. [ ] On sign-in, find the account and check the password against the stored hash. If it matches, give the browser a temporary token that expires.
5. [ ] Make a shared check in `backend/src/fin/api/dependencies.py` that tells other server features who is signed in. Make sign-out cancel the token.
6. [ ] Test valid registration, duplicate email, wrong password, expired session, and sign-out. Check that replies and logs contain no password or password hash.

**Done when** a correct password signs the user in, a wrong password is rejected, and a signed-out user cannot reuse the old token. Give Developer 1 the sign-in response and Developer 3 the sign-in check.

### Developer C — Check and save expenses through the server

Start in `backend/src/fin/services/transactions.py`, `backend/src/fin/schemas/transactions.py`, and `backend/src/fin/api/routes/transactions.py`.

1. [ ] Agree with Developer 1 on the fields the form sends and with Developer 4 on how to save and list expenses.
2. [ ] Check that the amount is positive and has at most two decimal places, the category is allowed, and the date exists on the calendar.
3. [ ] Convert amounts into whole cents. Check that **$12.50 becomes 1,250 cents**.
4. [ ] Use Developer 2's sign-in check to get the user ID. Pass it into every expense save and list request.
5. [ ] Connect add and list to Developer 4's storage functions. Return saved expenses newest first.
6. [ ] Test a valid expense, an empty list, zero, a negative amount, too many decimal places, an invalid date, and a request made while signed out.

**Done when** a valid expense comes back with the correct cents, invalid entries get a clear error, and every save and list uses the signed-in user's ID. Give Developer 1 the exact response fields.

### Developer D — Set up Python and save data

Start in `backend/pyproject.toml`, `backend/src/fin/main.py`, and `backend/src/fin/db/migrations/0001_users_and_transactions.sql`.

1. [ ] Set up Python, the project dependencies, and the server entry point. Write down how a teammate can start it from a clean folder.
2. [ ] Add a local SQLite database with users, Personal accounts, and transactions. Link each transaction to an account and each account to its user.
3. [ ] Make the server create the database when needed. Start it again and check that it keeps existing records.
4. [ ] Build the user and transaction storage functions in `backend/src/fin/repositories/`. Save a new user and their Personal account together. Limit every expense query to the signed-in user.
5. [ ] Connect storage to the account and expense features. Have Python serve the browser pages from the same server.
6. [ ] Test what happens if the Personal account fails to save. Check that the failed registration leaves no half-created user.
7. [ ] Use two test accounts to check separate expense lists. Stop and restart the server, sign in again, and check that the first user's expense survived.

**Done when** another developer can start the app from your instructions and repeat the two-user and restart checks on a fresh database.

**Team demo**

1. [ ] Create User A and User B. Sign in as A and save a $12.50 expense.
2. [ ] Sign out, sign in as B, and check that B's list is empty.
3. [ ] Restart FIN, sign back in as A, and check that the $12.50 expense is still there.
4. [ ] Sign out. Check that the server rejects a request made with the old sign-in token.