import { ProductProtocol } from './interfaces/ProductProtocol';

export class PrintedTShirtDecorator implements ProductProtocol {
  constructor(private product: ProductProtocol) {}

  get price(): number {
    return this.product.price + 10;
  }
  get name(): string {
    return this.product.name + ' (printed)';
  }
}
