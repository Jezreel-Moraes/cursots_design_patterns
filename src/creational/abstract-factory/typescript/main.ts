import { CustomerVehicleFactory } from './classes/factories/CustomerVehicleFactory';
import { EnterpriseVehicleFactory } from './classes/factories/EnterpriseVehicleFactory';

const customerFactory = new CustomerVehicleFactory();
const customer = customerFactory.createUser('Ana', 'Jaraguá');
const customerVehicle = customerFactory.createVehicle('Volvo');

console.log(customer);
customerVehicle.pickUp(customer.name);
console.log(customerVehicle);

console.log();

const enterpriseFactory = new EnterpriseVehicleFactory();
const enterpriser = enterpriseFactory.createUser('Joana', 'são Paulo');
const enterpriseVehicle = enterpriseFactory.createVehicle('Corsa');

console.log(enterpriser);
enterpriseVehicle.pickUp(enterpriser.name);
console.log(enterpriseVehicle);
