
from goal.goal_controller import GoalController


controller = GoalController()

# Create a new goal
goal = controller.create_goal("Vacation", 2000, "2027-06-01")

# Update the goal with ID 3
controller.update_goal(3, "Hawaii Vacation", 3000, 500, "2027-12-01")

# Display all goals
print("Goals after update:", controller.get_all_goals())

# Delete the goal with ID 3
controller.delete_goal(3)

# Display goals after deletion
print("Goals after deletion:", controller.get_all_goals())
