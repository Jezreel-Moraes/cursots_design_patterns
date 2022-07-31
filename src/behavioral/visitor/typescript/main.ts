import { Food } from './classes/food';
import { Medicine } from './classes/medicine';
import { Vehicle } from './classes/vehicle';
import { BrazilTaxVisitor } from './classes/visitors/BrazilTaxVisitor';
import { USATaxVisitor } from './classes/visitors/USATaxVisitor';
import { getMyCartTotalPrice, getMyCartTotalPriceWithTaxes } from './utils';

const banana = new Food('Banana', 10);
const tesla = new Vehicle('Tesla', 130_000);
const ibuprofen = new Medicine('Ibuprofen', 150);

const myCart = [banana, tesla, ibuprofen];

console.log('My cart total price:', getMyCartTotalPrice(myCart));
console.log(
  'My cart total price with Brazil taxes:',
  getMyCartTotalPriceWithTaxes(new BrazilTaxVisitor(), myCart),
);
console.log(
  'My cart total price with USA taxes:',
  getMyCartTotalPriceWithTaxes(new USATaxVisitor(), myCart),
);
