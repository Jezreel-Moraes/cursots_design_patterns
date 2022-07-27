export abstract class VehicleProtocol {
  constructor(private _name: string) {}

  get name(): string {
    return this._name;
  }

  abstract pickUp(userName: string): void;
  abstract get user(): string | null;
}
