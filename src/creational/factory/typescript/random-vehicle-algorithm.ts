import { BicycleFactory } from './classes/factories/BicycleFactory';
import { CarFactory } from './classes/factories/CarFactory';
import { Vehicle } from './classes/interfaces/VehicleProtocol';

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
