from classes.printed_tshirt_decorator import PrintedTShirtDecorator
from classes.tshirt import TShirt


def main():
    t_shirt = TShirt()
    print(t_shirt.get_price(), t_shirt.get_name())

    printed_t_shirt = PrintedTShirtDecorator(t_shirt)
    print(printed_t_shirt.get_price(), printed_t_shirt.get_name())

    re_printed_t_shirt = PrintedTShirtDecorator(printed_t_shirt)
    print(re_printed_t_shirt.get_price(), re_printed_t_shirt.get_name())


if __name__ == '__main__':
    main()
