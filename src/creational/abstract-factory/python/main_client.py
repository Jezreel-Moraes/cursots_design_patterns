from factories import *

factory1 = CustomerVehicleFactory1()
factory2 = CustomerVehicleFactory2()

c1 = factory1.create_customer('Joao', 'Joinville')
v1 = factory1.create_vehicle('Volvo')

print(c1.get_name())
print(c1.get_location())
c1.say_poggers()
print()
print(v1.get_name())
v1.pick_up(c1.get_name())
print(v1.get_customer())
print()

c2 = factory2.create_customer('Jonas', 'Cubatao')
v2 = factory2.create_vehicle('Vasco')

print(c2.get_name())
print(c2.get_location())
c2.say_poggers()
print()

print(v2.get_name())
v2.pick_up(c2.get_name())
print(v2.get_customer())
print()
