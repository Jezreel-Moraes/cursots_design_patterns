from classes.customer_budget import CustomerBudget
from classes.interfaces.base_budget_handler import BaseBudgetHandler


class DirectorBudgetHandler(BaseBudgetHandler):

    def handle(self, budget: CustomerBudget):
        if budget.price > 50000:
            return super().handle(budget)

        print("DirectorBudgetHandler: I can handle this budget")
        budget.approved = True
        return budget
