import { AbstractMeal } from './abstract-meal';
import { MealCompositeProtocol } from './interfaces/meal-composite-protocol';

export class MealBox implements MealCompositeProtocol {
  private readonly _children: AbstractMeal[] = [];

  getPrice(): number {
    return this._children.reduce((sum, meal) => sum + meal.getPrice(), 0);
  }

  add(...meals: AbstractMeal[]): void {
    meals.forEach((meal) => this._children.push(meal));
  }
}
