from typing import Protocol


class Iterator(Protocol):
    index: int
    last: int

    def __iter__(self) -> "Iterator":
        ...

    def __next__(self) -> None:
        ...

    def has_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...
