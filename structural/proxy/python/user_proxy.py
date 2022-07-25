from re import A
from typing import List

from admin_user import AdminUser
from system_protocols import UserAddressProtocol, UserProtocol


class UserProxy(UserProtocol):
    def __init__(self, first_name: str, user_name: str) -> None:
        super().__init__(first_name, user_name)
        self.real_user: AdminUser | None = None
        self.real_user_address: List[UserAddressProtocol] | None = None

    def create_user(self) -> AdminUser:
        return AdminUser(
            self.first_name, self.user_name)

    async def get_addresses(self) -> List[UserAddressProtocol]:
        if self.real_user is None:
            self.real_user = self.create_user()

        if self.real_user_address is None:
            self.real_user_address = await self.real_user.get_addresses()

        return self.real_user_address
