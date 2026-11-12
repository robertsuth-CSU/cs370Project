import sqlite3


class GoalDAO:

    def __init__(self, database="fin.db"):
        self.database = database

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                target_amount REAL NOT NULL,
                current_amount REAL NOT NULL,
                target_date TEXT
                )
                """)

        connection.commit()
        connection.close()

    def save_goal(self, goal):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        target_amount REAL NOT NULL,
        current_amount REAL NOT NULL,
        target_date TEXT
        )
        """)

        cursor.execute("""
        INSERT INTO goals (name, target_amount, current_amount, target_date)
        VALUES (?, ?, ?, ?)
        """, (
            goal.name,
            goal.target_amount,
            goal.current_amount,
            goal.target_date
        ))

        connection.commit()
        connection.close()


    #both the update_goal()will change the infromation associated with an exisitng
    #goal and then delete_goal() will remove a goal form the database using the ID

    def update_goal(self, goal_id, name, target_amount, current_amount, target_date):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE goals
        SET name = ?, target_amount = ?, current_amount = ?, target_date = ?
        WHERE id = ?
        """, (name, target_amount, current_amount, target_date, goal_id))

        connection.commit()
        connection.close()

        #will find the goal using the ID, update only its current_amount,
        #leave the goal name, target amount, and target date unchanged
        #save the changes in SQLite

    def update_current_savings(self, goal_id, current_amount):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE goals
        SET current_amount = ?
        WHERE id = ?
        """, (current_amount, goal_id))

        connection.commit()
        connection.close()

    def delete_goal(self, goal_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        DELETE FROM goals WHERE id = ?
        """, (goal_id,))
        connection.commit()
        connection.close()


    def get_all_goals(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM goals ORDER BY target_date IS NULL, target_date ASC")
        goals = cursor.fetchall()

        connection.close()

        return goals
