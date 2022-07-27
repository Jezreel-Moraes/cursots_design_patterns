from abc import ABC, abstractmethod
from typing import List

from classes.interfaces.user_address_protocol import UserAddressProtocol


class UserProtocol(ABC):
    def __init__(self, first_name: str, user_name: str) -> None:
        self.first_name = first_name
        self.user_name = user_name

    @abstractmethod
    async def get_addresses(self) -> List[UserAddressProtocol]: pass
