import { AbstractVisitor } from '../interfaces/AbstractVisitor';

export class BrazilTaxVisitor extends AbstractVisitor {
  protected foodTax = 20 / 100;
  protected vehicleTax = 32 / 100;
  protected medicineTax = 26 / 100;
}
