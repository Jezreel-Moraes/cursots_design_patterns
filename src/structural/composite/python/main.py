from classes.composite_validation import (ValidateCompositor, ValidateEmail,
                                          ValidateInt, ValidateString)
from classes.compositor import Compositor
from classes.leaf import Leaf


def normal_compositor():
    compositor = Compositor('Caixa de leite')
    leaf = Leaf('Leite', 3)

    print(f'Leaf price: {leaf.get_price()}')
    compositor.add(leaf, leaf, leaf)
    print(f'Compositor items: {compositor.children}')
    print(f'Compositor price: {compositor.get_price()}')


def validator_with_compositor():
    validator = ValidateCompositor()
    is_string = ValidateString()
    is_email = ValidateEmail()
    is_int = ValidateInt()

    validator.add(is_string, is_email, is_int)

    values = ['Olá', 'email@gmail.com', 3319]
    for value in values:
        print('>> VALIDATING:', value, '<<')
        validator.validate(value)
        print()


def main():
    normal_compositor()
    print()
    validator_with_compositor()


if __name__ == '__main__':
    main()
