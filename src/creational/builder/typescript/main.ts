import { MainDishBuilder } from './classes/main-dish-builder';

const mainDishBuilder = new MainDishBuilder();
const meal = mainDishBuilder.makeMeal().getMeal();
console.log(meal);
console.log(meal.getPrice(), '\n');

mainDishBuilder.reset();
const meal2 = mainDishBuilder.makeBeverage().makeDessert().getMeal();
console.log(meal2);
console.log(meal2.getPrice());
