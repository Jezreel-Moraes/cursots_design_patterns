class CustomerBudget:
    def __init__(self, price: int):
        self.approved = False
        self.price = price

    def __repr__(self) -> str:
        return f"CustomerBudget {{ price: {self.price}, approved: {self.approved} }}"