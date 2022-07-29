from classes.factories.delivery_factory import DeliveryFactory
from classes.interfaces.delivery_location_data import DeliveryLocationData


def deliveryContext(
    factory: DeliveryFactory,
    name: str,
    number: str,
    street: str,
    city: str,
) -> None:
    location = factory.create_location(DeliveryLocationData(city, street))
    location.deliver(name, number)
