import { AbstractVisitableProduct } from './interfaces/AbstractVisitableProduct';
import { VisitorProtocol } from './interfaces/VisitorProtocol';

export class Medicine extends AbstractVisitableProduct {
  getPriceWithTaxes(visitor: VisitorProtocol): number {
    return visitor.taxesForMedicines(this);
  }
}
