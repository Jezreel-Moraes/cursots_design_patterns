from shopping_order.shopping_order import ShoppingOrder


def main():
   shopping_order = ShoppingOrder()
   shopping_order.ship_order()
   print()

   shopping_order.approve_payment()
   shopping_order.ship_order()
   print()

   shopping_order.wait_payment()
   shopping_order.ship_order()
   print()

   shopping_order.reject_payment()
   print()

   shopping_order.approve_payment()
   print()

   shopping_order.wait_payment()
   print()

   shopping_order.reject_payment()
   print()

   shopping_order.ship_order()
   print()

if __name__ == '__main__':
   main()   