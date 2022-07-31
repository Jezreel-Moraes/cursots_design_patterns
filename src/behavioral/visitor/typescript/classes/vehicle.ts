import { AbstractVisitableProduct } from './interfaces/AbstractVisitableProduct';
import { VisitorProtocol } from './interfaces/VisitorProtocol';

export class Vehicle extends AbstractVisitableProduct {
  getPriceWithTaxes(visitor: VisitorProtocol): number {
    return visitor.taxesForVehicles(this);
  }
}
