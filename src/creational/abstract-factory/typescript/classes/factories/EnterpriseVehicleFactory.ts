import { Enterpriser } from '../Enterpriser';
import { EnterpriseVehicle } from '../EnterpriseVehicle';
import { UserProtocol } from '../interfaces/UserProtocol';
import { UserVehicleFactoryProtocol } from '../interfaces/UserVehicleFactoryProtocol';
import { VehicleProtocol } from '../interfaces/VehicleProtocol';

export class EnterpriseVehicleFactory implements UserVehicleFactoryProtocol {
  createUser(name: string, location: string): UserProtocol {
    return new Enterpriser(name, location);
  }
  createVehicle(name: string): VehicleProtocol {
    return new EnterpriseVehicle(name);
  }
}
