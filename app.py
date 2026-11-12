from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date
from goal.goal_controller import GoalController

#creates the actual flask application
app = Flask(__name__)
app.secret_key = "fin-secret-key"
#Conencts the Flask to the Financial Goals Package
goal_controller = GoalController()

#will display the financial goals webpage
@app.route("/")
def home():
    goals = goal_controller.get_all_goals()
    return render_template("index.html", goals=goals, today=date.today().isoformat())

@app.route("/create-goal", methods=["POST"])
def create_goal():

    name = request.form.get("goal_name")
    target_date = request.form.get("target_date") or None

    try:
        target_amount = float(request.form.get("target_amount"))
    except (ValueError, TypeError):
        return "Please enter a vlid target amount.", 400

    if not name or not name.strip():
        return "Goal name cannot be empty.", 400

    if target_amount <= 0:
        return "Target amount must be greater than zero.", 400

    if target_date:
        try:
            selected_date = date.fromisoformat(target_date)
        except ValueError:
            return "Please enter a valid target date.", 400

    if selected_date < date.today():
        return "Target date cannot be in the past.", 400

    goal_controller.create_goal(name, target_amount, target_date)

    return redirect(url_for("home"))

@app.route("/update-savings", methods=["POST"])
def update_savings():
    
    try:
        goal_id = int(request.form.get("goal_id"))
        current_amount = float(request.form.get("current_amount"))
    except (ValueError, TypeError):
        return "Please enter a vlid savings amount.", 400

    if current_amount < 0:
        return "Savings amount cannot be negative.", 400

    goal_controller.update_current_savings(goal_id, current_amount)

    return redirect(url_for("home"))

@app.route("/delete-goal", methods=["POST"])
def delete_goal():
    try:
        goal_id = int(request.form.get("goal_id"))
    except (ValueError, TypeError):
        return "Invalid goal ID.", 400
    
    goal_controller.delete_goal(goal_id)

    return redirect(url_for("home"))

# Receives updated financial goal information
@app.route("/edit-goal", methods=["POST"])
def edit_goal():

    name = request.form.get("goal_name")
    target_date = request.form.get("target_date") or None


    try:
        goal_id = int(request.form.get("goal_id"))
        target_amount = float(request.form.get("target_amount"))
    except (ValueError, TypeError):
        return "Please enter a valid goal ID and target amount.", 400
    
    if not name or not name.strip():
        return "Goal name cannot be empty.", 400

    if target_amount <= 0:
        return "Target amount must be greater than zero.", 400

    # Get the existing savings amount
    goals = goal_controller.get_all_goals()
    current_amount = 0
    current_target_date = None

    for goal in goals:
        if goal[0] == goal_id:
            current_amount = goal[3]
            current_target_date = goal[4]
            break

    if target_date:
        try:
            selected_date = date.fromisoformat(target_date)
        except ValueError:
            flash ("Please enter a valid target date.", "error")
            return redirect(url_for(home))

        if selected_date < date.today() and target_date != current_target_date:
            flash("Target date cannot be in the past.", "error")
            return redirect(url_for("home"))

    goal_controller.update_goal(
        goal_id, name, target_amount, current_amount, target_date
    )

    return redirect(url_for("home"))


#Will Run the application 
if __name__ == "__main__":
    app.run(debug=True)

#here the flask will import the flask framework
#it will then render_template which will allow flask to display HTML files
# app Flask(__name__) will create the application 
#@app.route("/") will define the homepage URL
#home() will run when someone vists the homepage 
#render_template() load the index.html file
#app.run(debug=True) will start the development server