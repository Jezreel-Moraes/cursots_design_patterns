from abc import ABC


class UserAddressProtocol(ABC):
    def __init__(self, street: str, number: int) -> None:
        self.street = street
        self.number = number

    def __repr__(self) -> str:
        return f'{{ street: {self.street}, number: {self.number}}}'
