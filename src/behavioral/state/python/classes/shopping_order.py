from classes.interfaces.shopping_order_state import ShoppingOrderState
from classes.order_states import OrderPending


class ShoppingOrder:
    def __init__(self) -> None:
        self.state: ShoppingOrderState = OrderPending(self)

    def get_state_name(self):
        return self.state.get_name()

    def set_state(self, state: ShoppingOrderState):
        self.state = state
        print(f'State changed to {self.get_state_name()}')

    def get_state(self):
        return self.state

    def approve_payment(self):
        self.state.approve_payment()

    def reject_payment(self):
        self.state.reject_payment()

    def wait_payment(self):
        self.state.wait_payment()

    def ship_order(self):
        self.state.ship_order()
