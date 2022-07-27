import { VehicleProtocol } from './interfaces/VehicleProtocol';

export class EnterpriseVehicle extends VehicleProtocol {
  private enterpriser: string | null = null;

  pickUp(userName: string): void {
    this.enterpriser = userName;
    console.log(`${this.name} is looking for ${userName}`);
  }

  get user(): string | null {
    return this.enterpriser;
  }
}
