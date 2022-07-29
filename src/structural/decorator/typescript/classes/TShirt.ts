import { ProductProtocol } from './interfaces/ProductProtocol';

export class TShirt implements ProductProtocol {
  private _price = 49.9;
  private _name = 'TShirt';

  get price(): number {
    return this._price;
  }
  get name(): string {
    return this._name;
  }
}
