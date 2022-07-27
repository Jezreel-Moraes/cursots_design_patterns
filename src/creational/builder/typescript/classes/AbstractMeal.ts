import { MealCompositeProtocol } from './interfaces/MealCompositeProtocol';

export class AbstractMeal implements MealCompositeProtocol {
  constructor(private name: string, private price: number) {}

  getPrice(): number {
    return this.price;
  }
}
