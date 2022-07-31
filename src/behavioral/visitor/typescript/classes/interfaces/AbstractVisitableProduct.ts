import { VisitableProductProtocol } from './VisitableProductProtocol';
import { VisitorProtocol } from './VisitorProtocol';

export abstract class AbstractVisitableProduct
  implements VisitableProductProtocol
{
  constructor(private _name: string, private _price: number) {}
  get name(): string {
    return this._name;
  }

  get price(): number {
    return this._price;
  }

  abstract getPriceWithTaxes(visitor: VisitorProtocol): number;
}
