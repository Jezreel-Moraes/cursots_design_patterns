from customer_budget import CustomerBudget
from base_budget_handler import BaseBudgetHandler

class SellerBudgetHandler(BaseBudgetHandler):
   
   def handle(self, budget: CustomerBudget):
      if budget.price > 1000: return super().handle(budget)
      
      print("SellerBudgetHandler: I can handle this budget")   
      budget.approved = True
      return budget   
         