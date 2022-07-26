import { MealBuilderProtocol } from './interfaces/meal-builder-protocol';
import { MealBox } from './meal-box';
import { Beans, Beverage, Dessert, Meat, Rice } from './meals';

export class MainDishBuilder implements MealBuilderProtocol {
  private _meal: MealBox = new MealBox();

  reset(): this {
    this._meal = new MealBox();
    return this;
  }

  getPrice(): number {
    return this._meal.getPrice();
  }

  getMeal(): MealBox {
    return this._meal;
  }

  makeRice(): this {
    const rice = new Rice('Arroz', 6);
    this._meal.add(rice);
    return this;
  }

  makeBeans(): this {
    const beans = new Beans('Feijão', 10);
    this._meal.add(beans);
    return this;
  }

  makeMeat(): this {
    const meat = new Meat('Carne', 12);
    this._meal.add(meat);
    return this;
  }

  makeMeal(): this {
    return this.makeRice().makeBeans().makeMeat();
  }
  makeBeverage(): this {
    const beverage = new Beverage('Bebida', 3);
    this._meal.add(beverage);
    return this;
  }
  makeDessert(): this {
    const dessert = new Dessert('Sobremesa', 12);
    this._meal.add(dessert);
    return this;
  }
}
