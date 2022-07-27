import { BicycleFactory } from './classes/factories/bicycle-factory';
import { CarFactory } from './classes/factories/car-factory';
import { Vehicle } from './classes/interfaces/vehicle-protocol';

const carFactory = new CarFactory();
const bicycleFactory = new BicycleFactory();
const vehicles = [
  carFactory.getVehicle('Celta'),
  carFactory.getVehicle('Corsa'),
  bicycleFactory.getVehicle('Bicycle'),
];

const randomInt = () => Math.floor(Math.random() * vehicles.length);

export const randomCarAlgorithm = (): Vehicle => {
  return vehicles[randomInt()];
};
