import asyncio

from admin_user import AdminUser
from user_proxy import UserProxy


async def with_proxy_as_cache():
    user = UserProxy('John', 'Doe')
    print("that's gonna take 2 seconds")
    print(await user.get_addresses())
    print()
    print("that's gonna repeat...")

    for _ in range(10):
        print(await user.get_addresses())
        print()


async def without_proxy():
    user = AdminUser('John', 'Doe')
    print("that's gonna take 2 seconds")
    print(await user.get_addresses())
    print()
    print("that's gonna repeat...")

    for _ in range(10):
        print(await user.get_addresses())
        print()


if __name__ == '__main__':
    asyncio.run(with_proxy_as_cache())
    asyncio.run(without_proxy())
