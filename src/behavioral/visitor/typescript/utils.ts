import { VisitableProductProtocol } from './classes/interfaces/VisitableProductProtocol';
import { VisitorProtocol } from './classes/interfaces/VisitorProtocol';

export const getMyCartTotalPrice = (
  cart: VisitableProductProtocol[],
): number => {
  return cart.reduce((sum, item) => sum + item.price, 0);
};

export const getMyCartTotalPriceWithTaxes = (
  visitor: VisitorProtocol,
  cart: VisitableProductProtocol[],
): number => {
  return cart.reduce((sum, item) => sum + item.getPriceWithTaxes(visitor), 0);
};
