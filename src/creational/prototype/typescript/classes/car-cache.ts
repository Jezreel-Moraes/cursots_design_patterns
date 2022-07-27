import { BigCar, SmallCar } from './cars';
import { Car } from './interfaces/car-protocol';

type Ids = typeof ids;
export type IdsKeys = keyof Ids;

export const ids = {
  SmallCar: 0,
  BigCar: 1,
};

export class CarsCache {
  private static readonly _cars: Record<number, Car> = {};

  static getCar(id: IdsKeys): Car {
    if (CarsCache._cars[ids[id]] === undefined) this.load(id);
    return CarsCache._cars[ids[id]].clone();
  }

  static load(id: IdsKeys): void {
    const loadDict = {
      SmallCar: this.loadSmallCar,
      BigCar: this.loadBigCar,
    };
    loadDict[id] && loadDict[id]();
  }

  static loadBigCar(): void {
    console.log('\nLoading BigCar');

    const bigCar = new BigCar();
    bigCar.id = ids.BigCar;
    CarsCache._cars[bigCar.id] = bigCar;

    console.log('finished loading\n');
  }

  static loadSmallCar(): void {
    console.log('\nLoading SmallCar');

    const smallCar = new SmallCar();
    smallCar.id = ids.SmallCar;

    CarsCache._cars[ids.SmallCar] = smallCar;

    console.log('finished loading\n');
  }
}
