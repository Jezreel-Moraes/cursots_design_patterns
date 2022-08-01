from classes.buyer import Buyer
from classes.mediator import Mediator
from classes.seller import Seller, SellerProduct


def main():
    mediator = Mediator()
    seller1 = Seller('Ronaldo')
    seller1.add_product(
        SellerProduct('1', 'House', 5_000_000.00),
        SellerProduct('2', 'Car', 40_000.00),
        SellerProduct('3', 'SmartPhone', 3_870.40)
    )

    seller2 = Seller('Augusto')
    seller2.add_product(
        SellerProduct('4', 'Apartment', 100_000_000.00),
        SellerProduct('5', 'TV', 2_000.00),
        SellerProduct('6', 'Chair', 287.40)
    )

    mediator.add_seller(seller1, seller2)
    buyer = Buyer('John', mediator)

    buyer.view_products()
    buyer.buy('2')
    buyer.buy('1')
    buyer.buy('7')

    buyer.view_products()

    seller1.buy('4')
    seller1.buy('3')
    seller1.view_products()


if __name__ == '__main__':
    main()
