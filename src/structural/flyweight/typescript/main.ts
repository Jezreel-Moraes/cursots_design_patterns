import { DeliveryFactory } from './classes/factories/DeliveryFactory';
import { deliveryContext } from './deliveryContext';

const factory = new DeliveryFactory();

deliveryContext(factory, 'John', '12345', 'Main Street', 'New York');
deliveryContext(factory, 'Ana', '145', 'Main Street', 'New York');
deliveryContext(factory, 'Jez', '1565', 'Street', 'Russia');

console.log();

console.log(factory.locations);
