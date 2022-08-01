from classes.data_structure import DataStructure
from classes.iterator_forward import IteratorForward
from classes.iterator_reversed import IteratorReversed


def main():
    data_structure = DataStructure(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    data_structure.set_iterator(IteratorForward(data_structure))

    a, b, c, *_ = data_structure
    print(a, b, c, '\n')
    data_structure.reset_iterator()

    for item in data_structure:
        print(item)

    print()

    data_structure.set_iterator(IteratorReversed(data_structure))

    a, b, c, *_ = data_structure
    print(a, b, c, '\n')
    data_structure.reset_iterator()

    for item in data_structure:
        print(item)


if __name__ == '__main__':
    main()
