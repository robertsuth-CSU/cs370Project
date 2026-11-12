#name will be for what the user is saving for 
#target_amount is how much money the user wants to save
#current_amount is how much the user has saved so far
#target_date: when the user hopes to reach the goal 
#calculate_remaining_amount(): how much more money they need 
#calculate_progress() calculate their progress as percentage

#Main purpose of this class is to represent indivdual fincanical goals and calculate progress

class Goal:
    def __init__(self, name, target_amount, current_amount =0.0, target_date=None):
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.target_date = target_date

    def calculate_remaining_amount(self):
        return self.target_amount - self.current_amount

    def calculate_progress(self):
        if self.target_amount <= 0:
            return 0

        return (self.current_amount / self.target_amount) * 100