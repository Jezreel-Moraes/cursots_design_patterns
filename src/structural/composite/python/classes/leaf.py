from classes.interfaces.leaf_protocol import LeafComponent


class Leaf(LeafComponent):
    def get_price(self) -> int:
        return self.price
