from classes.data_structure import DataStructure


class IteratorReversed:
    def __init__(self, data_structure: DataStructure) -> None:
        self.data_structure: DataStructure = data_structure
        self.index: int = data_structure.size() - 1
        self.last: int = -1

    def reset(self) -> None:
        self.index = self.data_structure.size() - 1

    def __iter__(self) -> "IteratorReversed":
        return self

    def __next__(self) -> str | int:
        if not self.has_next():
            raise StopIteration

        item: str | int = self.data_structure.items[self.index]
        self.index -= 1
        return item

    def has_next(self) -> bool:
        return self.index > self.last
