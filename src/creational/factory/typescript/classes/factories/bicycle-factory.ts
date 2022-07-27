import { Vehicle } from '../interfaces/vehicle-protocol';
import { Bicycle } from '../vehicles';
import { VehicleFactoryProtocol } from './vehicle-factory';

export class BicycleFactory extends VehicleFactoryProtocol {
  getVehicle(vehicleName: string): Vehicle {
    return new Bicycle(vehicleName);
  }
}
