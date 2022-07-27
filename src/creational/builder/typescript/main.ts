import { MainDishBuilder } from './classes/builders/MainDishBuilder';

const mainDishBuilder = new MainDishBuilder();
const meal = mainDishBuilder.makeMeal().getMeal();
console.log(meal);
console.log(meal.getPrice(), '\n');

mainDishBuilder.reset();
const meal2 = mainDishBuilder.makeBeverage().makeDessert().getMeal();
console.log(meal2);
console.log(meal2.getPrice());
