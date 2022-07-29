from classes.delivery_location import DeliveryLocation
from classes.interfaces.delivery_flyweight_protocol import \
    DeliveryFlyweightProtocol
from classes.interfaces.delivery_location_data import DeliveryLocationData


class DeliveryFactory:
    def __init__(self) -> None:
        self.locations: dict[str, DeliveryLocation] = {}

    @staticmethod
    def __create_id(data: DeliveryLocationData) -> str:
        return '_'.join(map(lambda value: value.replace(' ', '')
                            .lower(), [data.city, data.street]))

    def create_location(
        self,
        intrinsicState: DeliveryLocationData
    ) -> DeliveryFlyweightProtocol:

        key = self.__create_id(intrinsicState)
        if (key not in self.locations.keys()):
            self.locations[key] = DeliveryLocation(intrinsicState)
        return self.locations[key]

    def get_locations(self) -> dict[str, DeliveryLocation]:
        return dict(self.locations)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.__dict__}'
