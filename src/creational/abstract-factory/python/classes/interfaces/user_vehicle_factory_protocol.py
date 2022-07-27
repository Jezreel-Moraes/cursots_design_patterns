from abc import ABCMeta, abstractclassmethod

from classes.interfaces.user_protocol import UserProtocol
from classes.interfaces.vehicle_protocol import VehicleProtocol


class UserVehicleFactoryProtocol(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def create_user(name: str, location: str) -> UserProtocol:
        pass

    @staticmethod
    @abstractclassmethod
    def create_vehicle(name: str) -> VehicleProtocol:
        pass
