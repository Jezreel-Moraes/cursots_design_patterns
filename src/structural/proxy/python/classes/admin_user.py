import asyncio
from typing import List

from classes.interfaces.user_address_protocol import UserAddressProtocol
from classes.interfaces.user_protocol import UserProtocol
from classes.user_address import UserAddress


class AdminUser(UserProtocol):
    async def get_addresses(self) -> List[UserAddressProtocol]:
        await asyncio.sleep(2)
        return [
            UserAddress('Street 1', 1),
            UserAddress('Street 2', 2),
        ]
