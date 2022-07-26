export default null;
import { DatabaseSingleton } from './classes/Database';
import { db as moduleDB } from './module';

console.log('> From Class:\n');
const db = DatabaseSingleton.create();

db.add(
  { name: 'Carla', age: 21 },
  { name: 'Ana', age: 76 },
  { name: 'João', age: 84 },
  { name: 'Luiz', age: 25 },
);

const db1 = DatabaseSingleton.create();
db1.show();

console.log(db === moduleDB);
console.log();
console.log(moduleDB);
