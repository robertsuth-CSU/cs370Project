## Step 1 for the whole team

1. [ ] Put your names next to Developer A, B, C, and D below.
2. [ ] Agree on the information the screens send and receive. Registration sends a name, email, and password. Sign-in gives the app a session. An expense sends amount text, category, date, and an optional description. The saved expense comes back with an ID and its amount in cents.
3. [ ] Agree on the Python calls for registering, signing in, signing out, adding an expense, and listing expenses. Developer B owns the account section of `application.py`, and Developer C owns the expense section. Edit those sections separately and review the shared file together when combining work.

## Developer A — Build the screens

Start in `frontend/src/ui.py`. Record or automate the browser checks in `frontend/tests/test_browser.py`.

1. [ ] Make the registration and sign-in forms in NiceGUI. Give each field a clear label and show errors near the form.
2. [ ] Make the expense form with amount, category, date, and optional description. Add a list and total for saved expenses.
3. [ ] Try the screens with sample replies while Developers B and C build the real functions. Check loading, success, and error states.
4. [ ] Connect the forms to `application.py`. Keep the current session tied to that browser. After sign-in, load the user's expenses. After a save, show the updated list and total.
5. [ ] Clear the private view on sign-out or when a session expires. Try an empty form, a rejected expense, and a successful $12.50 save. Make sure a failed save leaves the list and total as they were.

**Done when** you can register, sign in, add a $12.50 expense, see it in the list and total, and sign out from the browser.

## Developer B — Build registration and sign-in

Work in the accounts section of `backend/src/application.py` and `backend/tests/unit/test_accounts.py`.

1. [ ] Agree with Developer D on how to save a new user and look up a user by email. Use a fake database reply until those functions are ready.
2. [ ] Validate the name, email, and password. Clean up email the same way at registration and sign-in so a different capitalization cannot create a second account.
3. [ ] Use the agreed password-hashing library to store a password hash. Call Developer D's function to save the user and their Personal account together.
4. [ ] Check the password at sign-in and start an expiring session when it matches. Give Developer C one shared function that returns the verified user ID for a valid session.
5. [ ] End the session on sign-out. Test duplicate email, correct and incorrect passwords, an expired session, and an attempt to use an old session after signing out. Check that replies and logs leave out passwords and password hashes.

**Done when** a user can register and sign in, a wrong password is rejected, and a signed-out or expired session cannot access expenses.

## Developer C — Build the expense rules

Work in the expenses section of `backend/src/application.py` and `backend/tests/unit/test_transactions.py`.

1. [ ] Agree with Developer A on the expense fields and allowed categories. Agree with Developer D on how to save and list expenses.
2. [ ] Check that the amount is positive and has at most two decimal places, the category is allowed, and the date is a real calendar date.
3. [ ] Convert the amount from text to whole cents. Check that **$12.50 becomes 1,250 cents**.
4. [ ] Use Developer B's session check to get the user ID before every save or list. Send that ID to Developer D's database functions and return the user's saved expenses newest first.
5. [ ] Test valid input, zero, a negative amount, too many decimal places, an invalid date, an empty list, and an attempt to save or list while signed out. Give Developer A the saved fields and error messages.

**Done when** a valid expense saves with the correct cents, bad inputs show a useful error, and every expense operation is limited to the signed-in user.

## Developer D — Set up Python and store the data

Start in `backend/src/db/database.py`, `backend/pyproject.toml`, and `backend/tests/integration/test_app.py`. Add the tested launch instructions to `README.md`.

1. [ ] Set up the Python environment and dependencies for NiceGUI, SQLAlchemy, and the agreed password library. Check that `ui.py` can call `application.py` and that the application can call `database.py`.
2. [ ] Define the users, Personal accounts, and expense records in Python. Link each expense to a Personal account and that account to its user. Store amounts as whole cents.
3. [ ] Set up a local SQLite file. Create the tables on first run and open the same file on later runs so saved data is available after a restart.
4. [ ] Build the functions for finding a user, saving a user and their Personal account together, and saving and listing expenses for a particular user.
5. [ ] Check that a failed registration leaves no half-created account. Use two users to verify separate expense lists, then restart and check that the first user's expense is still there.
6. [ ] Write down the setup and launch steps. Ask another teammate to follow them from a clean copy and run the demo.

**Done when** a teammate can start FIN from your instructions and repeat the restart and two-user checks.

## Put the work together

1. [ ] Developer D shares the database functions. Developers B and C connect their sections of `application.py` and run the Python checks.
2. [ ] Developer A connects the screens to the agreed application calls and repeats the browser checks.
3. [ ] Run the team demo together. Fix failures before marking Sprint 1 complete.

## Team demo

1. [ ] Create two test users, User A and User B. Sign in as User A and add a $12.50 expense. Check that it appears in the list and total.
2. [ ] Try an invalid amount and verify that the saved total stays at $12.50.
3. [ ] Sign out and sign in as User B. Confirm that User B's expense list is empty.
4. [ ] Restart FIN and sign back in as User A. Confirm that the $12.50 expense is still there.
5. [ ] Sign out. Confirm that the old session can no longer add or list expenses.
