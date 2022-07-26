from classes.interfaces.SingletonMeta import SingletonMeta
from classes.interfaces.UserProtocol import User


class SingletonDatabase(metaclass=SingletonMeta):
    _users: list = list()

    def add(self, user: User) -> None:
        self._users.append(user)

    def remove(self, index: int) -> int:
        return self._users.pop(index)

    def show(self):
        for user in self._users:
            print(user)
