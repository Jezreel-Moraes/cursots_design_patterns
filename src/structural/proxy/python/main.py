import asyncio

from classes.admin_user import AdminUser
from classes.user_proxy import UserProxy


async def with_proxy_as_cache():
    user = UserProxy('John', 'Doe')
    print("that's gonna take 2 seconds")
    print(await user.get_addresses(), '\n')

    print("that's gonna repeat 5 times")
    for _ in range(5):
        print(await user.get_addresses())


async def without_proxy():
    user = AdminUser('John', 'Doe')
    print("that's gonna take 2 seconds")
    print(await user.get_addresses(), '\n')

    print("that's gonna repeat 5 times:")
    for _ in range(5):
        print(await user.get_addresses())


def main():
    print('With proxy as cache:\n')
    asyncio.run(with_proxy_as_cache())
    print('\nWithout proxy:\n')
    asyncio.run(without_proxy())


if __name__ == '__main__':
    main()
