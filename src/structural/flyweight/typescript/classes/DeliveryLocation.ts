import { DeliveryFlyweight } from './interfaces/DeliveryFlyweight';
import { DeliveryLocationData } from './interfaces/DeliveryLocationData';

export class DeliveryLocation implements DeliveryFlyweight {
  constructor(private _intrinsicState: DeliveryLocationData) {}

  get intrinsicState(): DeliveryLocationData {
    return this._intrinsicState;
  }

  deliver(name: string, number: string): void {
    console.log(`Deliver to ${name}`);
    console.log(
      `On street ${this._intrinsicState.street},`,
      `city ${this._intrinsicState.city}`,
    );
    console.log(`Number: ${number}`);
    console.log(`---------------------------`);
  }
}
