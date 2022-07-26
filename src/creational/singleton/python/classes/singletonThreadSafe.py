from threading import Thread

from interfaces.SingletonMeta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    value: str = ''

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))

    process1.start()
    process2.start()
