from classes.interfaces.product_protocol import ProductProtocol
from classes.shopping_cart import ShoppingCart
from classes.strategies.default_discount import DefaultDiscount
from classes.strategies.new_discount import NewDiscount

shopping_cart = ShoppingCart()

shopping_cart.add_products(ProductProtocol("Product 1", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 3", 50))

shopping_cart.set_discount_strategy(DefaultDiscount())
shopping_cart.set_discount_strategy(NewDiscount())

print('Total:', shopping_cart.get_total())
print('Total with discount:', shopping_cart.get_total_with_discount())
