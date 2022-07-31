import { AbstractVisitableProduct } from './interfaces/AbstractVisitableProduct';
import { VisitorProtocol } from './interfaces/VisitorProtocol';

export class Food extends AbstractVisitableProduct {
  getPriceWithTaxes(visitor: VisitorProtocol): number {
    return visitor.taxesForFoods(this);
  }
}
