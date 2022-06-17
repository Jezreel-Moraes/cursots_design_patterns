from e_commerce import *

shopping_cart = ShoppingCart()

shopping_cart.add_products(ProductProtocol("Product 1", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))
shopping_cart.add_products(ProductProtocol("Product 2", 50))

shopping_cart.set_discount_strategy(DefaultDiscount())
shopping_cart.set_discount_strategy(NewDiscount())

print(shopping_cart.get_total())
print(shopping_cart.get_total_with_discount())