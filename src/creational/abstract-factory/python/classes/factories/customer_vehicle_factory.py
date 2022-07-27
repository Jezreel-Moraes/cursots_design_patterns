from classes.customer import Customer
from classes.customer_vehicle import CustomerVehicle
from classes.interfaces.user_protocol import UserProtocol
from classes.interfaces.user_vehicle_factory_protocol import \
    UserVehicleFactoryProtocol
from classes.interfaces.vehicle_protocol import VehicleProtocol


class CustomerVehicleFactory(UserVehicleFactoryProtocol):
    @staticmethod
    def create_user(name: str, location: str) -> UserProtocol:
        return Customer(name, location)

    @staticmethod
    def create_vehicle(name: str) -> VehicleProtocol:
        return CustomerVehicle(name)
