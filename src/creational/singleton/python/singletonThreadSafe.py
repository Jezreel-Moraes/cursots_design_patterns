from singleton_meta import SingletonMeta
from threading import Thread
from time import sleep, perf_counter

class Teste(metaclass=SingletonMeta):
   value: str = None

   def __init__(self, value: str) -> None:
      self.value = value

   def some_business_logic(self):
      pass


class Singleton(metaclass=SingletonMeta):
   value: str = None


   def __init__(self, value: str) -> None:
         self.value = value

   def some_business_logic(self):
      pass

def test_singleton(value: str) -> None:
   singleton = Singleton(value)
   print(singleton.value)

def test_teste(value: str) -> None:
   singleton = Teste(value)
   print(singleton.value)
    
if __name__ == "__main__":
   process1 = Thread(target=test_singleton, args=("FOO",))
   process2 = Thread(target=test_singleton, args=("BAR",))

   process1.start()
   process2.start()