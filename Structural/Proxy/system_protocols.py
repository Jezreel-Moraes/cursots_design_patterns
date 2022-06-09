from typing import List
from abc import ABC, abstractmethod

class UserAddressProtocol():
    def __init__(self, street: str, number: int) -> None:
        self.street = street
        self.number = number
    
    def __repr__(self) -> str:
        return f'{{ street: {self.street}, number: {self.number}}}'
        
class UserProtocol(ABC):
    def __init__(self, first_name: str, user_name: str) -> None:
        self.first_name = first_name
        self.user_name = user_name
        
    @abstractmethod
    async def get_addresses(self) -> List[UserAddressProtocol]: pass
    
    