export abstract class UserProtocol {
  constructor(private _name: string, private _location: string) {}

  get name(): string {
    return this._name;
  }

  get location(): string {
    return this._location;
  }
}
