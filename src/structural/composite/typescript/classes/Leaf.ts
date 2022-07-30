import { LeafProtocol } from './interfaces/LeafProtocol';

export class Leaf implements LeafProtocol {
  constructor(private _price: number) {}

  get price(): number {
    return this._price;
  }
}
