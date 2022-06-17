from brazil_tax_visitor import BrazilTaxVisitor
from usa_tax_visitor import USATaxVisitor
from tax_visitor_protocol import TaxVisitor
from food import Food
from vehicle import Vehicle
from medicine import Medicine


def get_my_cart_total_price(cart: list) -> float:
   return sum(item.get_price() for item in cart)

def get_my_cart_price_with_taxes(visitor: TaxVisitor, cart: list) -> float:
   return sum(item.get_price_with_taxes(visitor) for item in cart)

banana = Food('Banana', 10)
tesla = Vehicle('Tesla', 130_000)
ibuprofen = Medicine('Ibuprofen', 150)

my_cart = [banana, tesla, ibuprofen]

print('My cart total price:', get_my_cart_total_price(my_cart))

print('My cart price with Brazil taxes:', get_my_cart_price_with_taxes(BrazilTaxVisitor(), my_cart))

print('My cart price with USA taxes:', get_my_cart_price_with_taxes(USATaxVisitor(), my_cart))