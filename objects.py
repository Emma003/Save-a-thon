
class Profile:
    def __init__(self, discordID, name, salary, utility_bills, transport, housing, budget_plan):
        self.discordID = discordID
        self.name = name
        self.salary = salary
        self.utility_bills = utility_bills
        self.transport = transport
        self.housing = housing
        self.budget_plan = budget_plan

class Goal:
    def __init__(self, discordID, name, title, cost, deadline, starting_contribution, monthly_contribution):
        self.discordID = discordID
        self.name = name
        self.title = title
        self.cost = cost
        self.deadline = deadline
        self.starting_contribution = starting_contribution
        self.monthly_contribution = monthly_contribution

class Expense:
    def __init__(self, discordID, name, category, amount):
        self.discordID = discordID
        self.name = name
        self.category = category
        self.amount = amount