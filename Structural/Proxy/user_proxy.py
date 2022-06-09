from system_protocols import UserProtocol, UserAddressProtocol
from admin_user import AdminUser
from typing import List

class UserProxy(UserProtocol):
   def __init__(self, first_name: str, user_name: str) -> None:
      super().__init__(first_name, user_name)
      self.real_user: UserProtocol | None = None
      self.real_user_address: List[UserAddressProtocol] | None = None
   
   def create_user(self) -> None:
      if not self.real_user is None: return
      self.real_user = AdminUser(self.first_name, self.user_name)
      
   async def get_addresses(self) -> List[UserAddressProtocol]:
      self.create_user()
      if self.real_user_address is None: 
         self.real_user_address = await self.real_user.get_addresses()
         
      return self.real_user_address