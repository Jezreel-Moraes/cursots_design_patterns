from singleton_meta import SingletonMeta

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

if __name__ == "__main__":
   singleton1 = Singleton("FOO")
   print(singleton1.value)
   singleton2 = Singleton("BAR")    
   print(singleton2.value)
   teste1 = Teste("BAR")
   print(teste1.value)
