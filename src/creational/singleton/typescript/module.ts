import { DatabaseSingleton } from './classes/Database';

const db = DatabaseSingleton.create();

db.add({ name: 'Cris', age: 12 });
db.add({ name: 'Rosana', age: 67 });
db.add({ name: 'Cleber', age: 48 });
db.add({ name: 'Bruno', age: 52 });

export { db };
