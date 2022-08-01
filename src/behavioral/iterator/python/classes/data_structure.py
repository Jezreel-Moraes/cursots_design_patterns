from dataclasses import dataclass, field

from classes.interfaces.iterator_protocol import Iterator


@dataclass
class DataStructure:
    items: list[str | int] = field(default_factory=list[str | int])
    iterator: Iterator | None = None

    def add_item(self, *items: str | int) -> None:
        self.items.extend(items)

    def get_items(self) -> list[str | int]:
        return self.items

    def size(self) -> int:
        return len(self.items)

    def set_iterator(self, iterator: Iterator) -> None:
        self.iterator = iterator

    def __iter__(self) -> Iterator:
        return self.iterator

    def reset_iterator(self) -> None:
        if self.iterator:
            self.iterator.reset()
