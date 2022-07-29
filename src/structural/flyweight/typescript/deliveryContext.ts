import { DeliveryFactory } from './classes/factories/DeliveryFactory';

export const deliveryContext = (
  factory: DeliveryFactory,
  name: string,
  number: string,
  street: string,
  city: string,
): void => {
  const location = factory.createLocation({ city, street });
  location.deliver(name, number);
};
