import { Customer } from '../Customer';
import { CustomerVehicle } from '../CustomerVehicle';
import { UserProtocol } from '../interfaces/UserProtocol';
import { UserVehicleFactoryProtocol } from '../interfaces/UserVehicleFactoryProtocol';
import { VehicleProtocol } from '../interfaces/VehicleProtocol';

export class CustomerVehicleFactory implements UserVehicleFactoryProtocol {
  createUser(name: string, location: string): UserProtocol {
    return new Customer(name, location);
  }
  createVehicle(name: string): VehicleProtocol {
    return new CustomerVehicle(name);
  }
}
