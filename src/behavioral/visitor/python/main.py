from classes.food import Food
from classes.interfaces.product_protocol import VisitableProductProtocol
from classes.interfaces.tax_visitor_protocol import TaxVisitor
from classes.medicine import Medicine
from classes.vehicle import Vehicle
from classes.visitors.brazil_tax_visitor import BrazilTaxVisitor
from classes.visitors.usa_tax_visitor import USATaxVisitor


def get_my_cart_total_price(cart: list[VisitableProductProtocol]) -> float:
    return sum(item.get_price() for item in cart)


def get_my_cart_price_with_taxes(
    visitor: TaxVisitor,
    cart: list[VisitableProductProtocol]
) -> float:
    return sum(item.get_price_with_taxes(visitor) for item in cart)


banana = Food('Banana', 10)
tesla = Vehicle('Tesla', 130_000)
ibuprofen = Medicine('Ibuprofen', 150)

my_cart = [banana, tesla, ibuprofen]

print('My cart total price:', get_my_cart_total_price(my_cart))

print('My cart price with Brazil taxes:',
      get_my_cart_price_with_taxes(BrazilTaxVisitor(), my_cart))

print('My cart price with USA taxes:',
      get_my_cart_price_with_taxes(USATaxVisitor(), my_cart))
