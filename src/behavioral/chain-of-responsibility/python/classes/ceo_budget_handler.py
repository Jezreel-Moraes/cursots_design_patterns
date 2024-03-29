from classes.customer_budget import CustomerBudget
from classes.interfaces.base_budget_handler import BaseBudgetHandler


class CEOBudgetHandler(BaseBudgetHandler):

    def handle(self, budget: CustomerBudget):
        print("CEOBudgetHandler: I can handle any budget")
        budget.approved = True
        return budget
