export default null;

class Person {
  constructor(public name: string) {}
}

class Student {
  constructor(public name: string) {}
}

export class SingletonPerson {
  private static _instance: Person | null = null;

  static create(name: string): Person {
    if (!this._instance) this._instance = new Person(name);
    return this._instance;
  }
}

export class SingletonStudent {
  private static _instance: Student | null = null;

  static create(name: string): Student {
    if (!this._instance) this._instance = new Student(name);
    return this._instance;
  }
}

class Singleton {
  private static readonly _instance: Record<string, any> = {};

  static create<T>(type: new (...args: any[]) => T, ...args: any[]): T {
    if (!this._instance[type.name]) {
      this._instance[type.name] = new type(...args);
    }
    return this._instance[type.name];
  }

  static get instance() {
    return this._instance;
  }
}

const student1 = Singleton.create(Student, 'estudante 1');
const student2 = Singleton.create(Student, 'estudante 2');

console.log(student1 === student2);
console.log(student2);

const person1 = Singleton.create(Person, 'pessoa 1');
const person2 = Singleton.create(Person, 'pessoa 2');

console.log(person1 === person2);
console.log(person2);

console.log(Singleton.instance);
