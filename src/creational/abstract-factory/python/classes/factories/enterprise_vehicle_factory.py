from classes.enterprise_vehicle import EnterpriseVehicle
from classes.enterpriser import Enterpriser
from classes.interfaces.user_protocol import UserProtocol
from classes.interfaces.user_vehicle_factory_protocol import \
    UserVehicleFactoryProtocol
from classes.interfaces.vehicle_protocol import VehicleProtocol


class EnterpriseVehicleFactory(UserVehicleFactoryProtocol):
    @staticmethod
    def create_user(name: str, location: str) -> UserProtocol:
        return Enterpriser(name, location)

    @staticmethod
    def create_vehicle(name: str) -> VehicleProtocol:
        return EnterpriseVehicle(name)
