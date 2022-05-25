from abc import ABCMeta, abstractmethod
import copy
from time import perf_counter

class Cars(metaclass = ABCMeta):
     
    def __init__(self):
        
        # some heavy processing
        for i in range(100):
            for n in range(100):
                if i != 0 and n != 0 and i % n != 0: m = i*n
        print(m)
        
        self.id = None
        self.type = None
 
    @abstractmethod
    def display_name(self):
        pass
 
    def set_type(self, type: str):
        self.type = type
 
    def get_type(self):
        return self.type
 
    def get_id(self):
        return self.id
 
    def set_id(self, id):
        self.id = id
 
    def clone(self):
        return copy.copy(self)
 
class SmallCar(Cars):
    def __init__(self):
        super().__init__()
        self.type = "SmallCar"
 
    def display_name(self):
        print("Inside SmallCar:display_name() method")
 
class BigCar(Cars):
    def __init__(self):
        super().__init__()
        self.type = "BigCar"
 
    def display_name(self):
        print("Inside BigCar:display_name() method.")

class CarsCache:
     
    cars = {}
 
    @staticmethod
    def get_car(id):
        if not CarsCache.cars: CarsCache.__load()
        
        CAR = CarsCache.cars.get(id, None)
        return CAR.clone()
 
    def __load():
        print('\nloading')
        bigCar = BigCar()
        bigCar.set_id("1")
        CarsCache.cars[bigCar.get_id()] = bigCar
 
        smallCar = SmallCar()
        smallCar.set_id("2")
        CarsCache.cars[smallCar.get_id()] = smallCar

def test_one():
    car1 = CarsCache.get_car("1")
    print(car1.get_type())
 
    car2 = CarsCache.get_car("1")
    print(car2.get_type())
    
    car2.set_type('carrao')
    print(car2.get_type())
    print(car1.get_type())
    
    print(car1 is car2)
    print(f'{car1=} \n {car2=}')
    
def test_two():
    bcar = None
    scar = None
    
    start = perf_counter()
    for c in range(5):
        bcar = BigCar()
        bcar.set_id("1")
        
        scar = SmallCar()    
        scar.set_id("2")
    end = perf_counter()
    print(f'time 1: {end-start} ms')
    print(bcar.type)
    print(scar.type)
    
    bcar = None
    scar = None
    
    start = perf_counter()
    for c in range(5):
        bcar = CarsCache.get_car('1')
        scar = CarsCache.get_car('2')
    end = perf_counter()
    print(f'time 2: {end-start} ms')
    print(bcar.type)
    print(scar.type)
       
if __name__ == '__main__': 
    # test_one()
    test_two()
    