import { Vehicle } from '../interfaces/VehicleProtocol';
import { Bicycle } from '../Vehicles';
import { VehicleFactoryProtocol } from './VehicleFactory';

export class BicycleFactory extends VehicleFactoryProtocol {
  getVehicle(vehicleName: string): Vehicle {
    return new Bicycle(vehicleName);
  }
}
