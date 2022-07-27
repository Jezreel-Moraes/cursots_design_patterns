import { CarsCache } from './classes/car-cache';
import { SmallCar } from './classes/cars';

const carList = [];

console.log('without cache/prototype:');
for (let index = 0; index < 5; index++) {
  const car = new SmallCar();
  car.id = 0;
  carList.push(car);
}

console.log(carList, '\n');
carList.length = 0;

console.log('with cache/prototype:');
for (let index = 0; index < 5; index++) {
  carList.push(CarsCache.getCar('BigCar'));
}
console.log(carList);
