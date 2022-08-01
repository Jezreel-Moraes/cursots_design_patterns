from classes.ceo_budget_handler import CEOBudgetHandler
from classes.customer_budget import CustomerBudget
from classes.director_budget_handler import DirectorBudgetHandler
from classes.manager_budget_handler import ManagerBudgetHandler
from classes.seller_budget_handler import SellerBudgetHandler


def main():
    customer_budget = CustomerBudget(5001)
    print(customer_budget)

    seller = SellerBudgetHandler()
    seller \
        .set_next_handler(ManagerBudgetHandler()) \
        .set_next_handler(DirectorBudgetHandler()) \
        .set_next_handler(CEOBudgetHandler())

    seller.handle(customer_budget)
    print(customer_budget)


if __name__ == "__main__":
    main()
