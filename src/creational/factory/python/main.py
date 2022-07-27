from faker import Faker
from random_vehicle_algorithm import randomCarAlgorithm

faker = Faker()

for _ in range(10):
    vehicle = randomCarAlgorithm()
    vehicle.pick_up(faker.name())
    vehicle.stop()
    print('---------------------------')
