import { UserProtocol } from './UserProtocol';
import { VehicleProtocol } from './VehicleProtocol';

export interface UserVehicleFactoryProtocol {
  createUser(name: string, location: string): UserProtocol;
  createVehicle(name: string): VehicleProtocol;
}
