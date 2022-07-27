import { Vehicle } from '../interfaces/vehicle-protocol';
import { Car } from '../vehicles';
import { VehicleFactoryProtocol } from './vehicle-factory';

export class CarFactory extends VehicleFactoryProtocol {
  getVehicle(vehicleName: string): Vehicle {
    return new Car(vehicleName);
  }
}
