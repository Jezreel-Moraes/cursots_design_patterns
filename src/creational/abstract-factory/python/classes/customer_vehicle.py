from classes.interfaces.vehicle_protocol import VehicleProtocol


class CustomerVehicle(VehicleProtocol):
    def pick_up(self, user_name: str) -> None:
        self.customer = user_name
        print(f'{self.get_name()} is looking for {user_name}')

    def get_user(self):
        return self.customer if self.customer else None
