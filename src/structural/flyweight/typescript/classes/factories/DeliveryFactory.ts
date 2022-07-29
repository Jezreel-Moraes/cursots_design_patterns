import { DeliveryLocation } from '../DeliveryLocation';
import { DeliveryFlyweight as DeliveryFlyweightProtocol } from '../interfaces/DeliveryFlyweight';
import { DeliveryLocationData } from '../interfaces/DeliveryLocationData';

export class DeliveryFactory {
  private readonly _locations: Record<string, DeliveryLocation> = {};

  private createId(data: DeliveryLocationData): string {
    return [data.city, data.street]
      .map((value: string) => {
        return value.replace(/\s/g, '').toLowerCase();
      })
      .join('_');
  }

  get locations(): Record<string, DeliveryLocation> {
    return this._locations;
  }

  createLocation(
    intrinsicState: DeliveryLocationData,
  ): DeliveryFlyweightProtocol {
    const key = this.createId(intrinsicState);
    if (!this._locations[key])
      this._locations[key] = new DeliveryLocation(intrinsicState);

    return this._locations[key];
  }
}

const d = new DeliveryFactory();
d.createLocation({ city: 'Joinville', street: 'Inambu' });
