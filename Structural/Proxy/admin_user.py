import asyncio
from typing import List
from system_protocols import UserProtocol, UserAddressProtocol

class AdminUser(UserProtocol):
   async def get_addresses(self) -> List[UserAddressProtocol]:
      await asyncio.sleep(2)
      return [
         UserAddressProtocol('Street 1', 1),
         UserAddressProtocol('Street 2', 2),
         ]
   