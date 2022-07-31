import { VisitorProtocol } from './VisitorProtocol';

export interface VisitableProductProtocol {
  getPriceWithTaxes(visitor: VisitorProtocol): number;
  get name(): string;
  get price(): number;
}
