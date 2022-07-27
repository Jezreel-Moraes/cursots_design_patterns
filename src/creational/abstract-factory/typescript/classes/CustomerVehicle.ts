import { VehicleProtocol } from './interfaces/VehicleProtocol';

export class CustomerVehicle extends VehicleProtocol {
  private customer: string | null = null;

  pickUp(userName: string): void {
    this.customer = userName;
    console.log(`${this.name} is looking for ${userName}`);
  }

  get user(): string | null {
    return this.customer;
  }
}
