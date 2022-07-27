from classes.interfaces.vehicle_factory_protocol import VehicleFactoryProtocol
from classes.interfaces.vehicle_protocol import Vehicle
from classes.vehicles import Car


class CarFactory(VehicleFactoryProtocol):
    def get_vehicle(self, vehicle_name: str) -> Vehicle:
        return Car(vehicle_name)
