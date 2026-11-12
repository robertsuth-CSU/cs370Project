# will handle the all the infromation that the user inputted for thier financail goals such as 
# retrieving progress information and checks if the savings updated

#update_progress() will update how much the user has saved
#get_remaining_amount() will find how much money is left to save
#get_goal_summary() will collct all the goal information into one summary

class GoalService:

    def update_progress(self, goal, new_amount):
        if new_amount < 0:
            raise ValueError("Savings amount cannot be negative.")

        goal.current_amount = new_amount

        return goal.calculate_progress()

    def get_remaining_amount(self, goal):
        return goal.calculate_remaining_amount()

    def get_goal_summary(self, goal):
        return {
            "name": goal.name,
            "target_amount": goal.target_amount,
            "current_amount": goal.current_amount,
            "remaining_amount": goal.calculate_remaining_amount(),
            "progress": goal.calculate_progress(),
            "target_date": goal.target_date
        }