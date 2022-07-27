import { Vehicle } from '../interfaces/vehicle-protocol';

export abstract class VehicleFactoryProtocol {
  abstract getVehicle(vehicleName: string): Vehicle;

  pickUp(customerName: string, vehicleName: string): Vehicle {
    const car = this.getVehicle(vehicleName);
    car.pickUp(customerName);
    return car;
  }
}
