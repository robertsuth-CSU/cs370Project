#this will handle requests such as creating a financial goal, view exisitng goals,
#update a goal, delete a goal, and view goal progress

#main points of each part:
#GoalCOntroller recieves the request
#GoalDAO communicates with the database
#SQLite stores the updated savings amount

from .goal import Goal 
from .goal_service import GoalService
from .goal_dao import GoalDAO

class GoalController:

    def __init__(self):
        self.service = GoalService()
        self.dao = GoalDAO()

    def create_goal(self, name, target_amount, target_date = None):
        goal = Goal(name, target_amount, 0.0, target_date)

        self.dao.save_goal(goal)

        return goal

    def get_all_goals(self):
        return self.dao.get_all_goals()

    def update_goal(self, goal_id, name, target_amount, current_amount, target_date):
        self.dao.update_goal(
            goal_id, name, target_amount, current_amount, target_date
        )
    
    def update_current_savings(self, goal_id, current_amount):
        self.dao.update_current_savings(goal_id, current_amount)

    def delete_goal(self, goal_id):
        self.dao.delete_goal(goal_id)

    def update_goal_progress(self, goal, new_amount):
        return self.service.update_progress(goal, new_amount)

    def get_goal_summary(self, goal):
        return self.service.get_goal_summary(goal)

