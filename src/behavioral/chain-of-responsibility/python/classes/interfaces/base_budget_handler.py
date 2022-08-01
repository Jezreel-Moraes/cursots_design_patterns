from classes.customer_budget import CustomerBudget


class BaseBudgetHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, budget: CustomerBudget):
        if self.next_handler:
            self.next_handler.handle(budget)
        return budget
