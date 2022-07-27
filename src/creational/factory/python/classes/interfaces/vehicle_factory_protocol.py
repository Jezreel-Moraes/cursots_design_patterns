from abc import ABCMeta, abstractclassmethod

from classes.interfaces.vehicle_protocol import Vehicle


class VehicleFactoryProtocol(metaclass=ABCMeta):
    @abstractclassmethod
    def get_vehicle(self, vehicle_name: str) -> Vehicle: pass

    def pick_up(self, customer_name: str, vehicle_name: str) -> Vehicle:
        car = self.get_vehicle(vehicle_name)
        car.pick_up(customer_name)
        return car
