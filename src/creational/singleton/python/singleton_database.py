from singleton_meta import SingletonMeta
from threading import Thread

class User():
        
    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        
    def __repr__(self) -> str: 
        return str(self.__dict__)
        
class SingletonDataBase(metaclass=SingletonMeta):
    _users : list = list()

    def add(self, user : User) -> None:
        self._users.append(user)
        
    def remove(self, index : int) -> int:
        return self._users.pop(index)

    def show(self):
        for user in self._users:
            print(user)
        
if __name__ == "__main__":
    db1 = SingletonDataBase()
    db1.add(User(name="Jorge", age=12)) 
    db1.add(User(name="Ana", age=45))
    db1.add(User(name="Rosana", age=52))
    db1.remove(1)
    
    
    db2 = SingletonDataBase()
    db2.show()
    
    print(db1 == db2)