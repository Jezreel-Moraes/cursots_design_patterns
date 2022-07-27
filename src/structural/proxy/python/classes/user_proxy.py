from typing import List

from classes.admin_user import AdminUser
from classes.interfaces.user_address_protocol import UserAddressProtocol
from classes.interfaces.user_protocol import UserProtocol


class UserProxy(UserProtocol):
    __real_user: AdminUser | None = None
    __real_user_address: List[UserAddressProtocol] | None = None

    def create_user(self) -> AdminUser:
        return AdminUser(self.first_name, self.user_name)

    async def get_addresses(self) -> List[UserAddressProtocol]:
        if self.__real_user is None:
            self.__real_user = self.create_user()

        if self.__real_user_address is None:
            self.__real_user_address = await self.__real_user.get_addresses()

        return self.__real_user_address
