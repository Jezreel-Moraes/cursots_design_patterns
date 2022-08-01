from classes.customer_budget import CustomerBudget
from classes.interfaces.base_budget_handler import BaseBudgetHandler


class ManagerBudgetHandler(BaseBudgetHandler):

    def handle(self, budget: CustomerBudget):
        if budget.price > 5000:
            return super().handle(budget)

        print("ManagerBudgetHandler: I can handle this budget")
        budget.approved = True
        return budget
