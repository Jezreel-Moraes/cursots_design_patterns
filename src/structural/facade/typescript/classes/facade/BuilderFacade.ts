import { MainDishBuilder } from '../../../../../creational/builder/typescript/classes/builders/MainDishBuilder';
import { MealBox } from '../../../../../creational/builder/typescript/classes/MealBox';
import {
  Beans,
  Meat,
  Rice,
} from '../../../../../creational/builder/typescript/classes/Meals';
import { BuilderFacadeProtocol } from '../interfaces/BuilderFacadeProtocol';

export class BuilderFacade implements BuilderFacadeProtocol {
  readonly mainDishBuilder = new MainDishBuilder();

  readonly rice = new Rice('Arroz', 5);
  readonly beans = new Beans('Feijão', 10);
  readonly meat = new Meat('Carne', 20);

  makeMealWithTwoBuilders(): void {
    const meal1 = this.mainDishBuilder.makeMeal().makeDessert().getMeal();
    console.log(meal1);
    console.log(meal1.getPrice());

    const meal2 = this.mainDishBuilder.makeMeal().makeDessert().getMeal();
    console.log(meal2);
    console.log(meal2.getPrice());
  }

  makeMealWithoutBuilder(): void {
    const mealBox = new MealBox();
    mealBox.add(this.rice, this.beans, this.meat);
    console.log(mealBox);
    console.log(mealBox.getPrice());
  }
}
