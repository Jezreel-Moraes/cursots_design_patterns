import { Vehicle } from '../interfaces/VehicleProtocol';
import { Car } from '../Vehicles';
import { VehicleFactoryProtocol } from './VehicleFactory';

export class CarFactory extends VehicleFactoryProtocol {
  getVehicle(vehicleName: string): Vehicle {
    return new Car(vehicleName);
  }
}
