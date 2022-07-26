from classes.interfaces.UserProtocol import User
from classes.singleton_database import SingletonDatabase


def main() -> None:
    db1 = SingletonDatabase()
    db1.add(User(name="Jorge", age=12))
    db1.add(User(name="Ana", age=45))
    db1.add(User(name="Rosana", age=52))
    db1.remove(1)

    db2 = SingletonDatabase()
    db2.show()

    print(db1 == db2)


if __name__ == "__main__":
    main()
