import { randomCarAlgorithm } from './random-vehicle-algorithm';

const names = ['Ana', 'Carla', 'Amanada', 'Maria', 'José', 'Carlos', 'Robson'];

for (const name of names) {
  const vehicle = randomCarAlgorithm();
  vehicle.pickUp(name);
  vehicle.stop();
  console.log('-----------------------------------');
}
