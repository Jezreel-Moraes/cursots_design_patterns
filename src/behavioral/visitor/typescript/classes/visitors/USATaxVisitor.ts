import { AbstractVisitor } from '../interfaces/AbstractVisitor';

export class USATaxVisitor extends AbstractVisitor {
  protected foodTax = 15 / 100;
  protected vehicleTax = 20 / 100;
  protected medicineTax = 46 / 100;
}
