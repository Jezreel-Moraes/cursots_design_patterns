from classes.interfaces.vehicle_protocol import VehicleProtocol


class EnterpriseVehicle(VehicleProtocol):
    def pick_up(self, user_name: str) -> None:
        self.enterpriser = user_name
        print(f'{self.get_name()} is looking for {user_name}')

    def get_user(self):
        return self.enterpriser if self.enterpriser else None
