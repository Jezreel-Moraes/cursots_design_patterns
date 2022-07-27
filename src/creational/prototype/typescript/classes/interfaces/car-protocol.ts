import { IdsKeys } from '../car-cache';

type ID = number | null;
type TYPE = IdsKeys | null;

export abstract class Car {
  [x: string]: any;
  constructor(protected _type: TYPE = null, protected _id: ID = null) {
    let _ = 0;
    for (let i = 0; i < 100000; i++)
      for (let j = 0; j < 10000; j++)
        if (i != 0 && j != 0 && i % j != 0) _ += i * j;
    console.log(' > Creating new car:', this.__proto__.constructor.name);
  }

  set type(type: TYPE) {
    if (type === null) return;
    this._type = type;
  }

  get type(): TYPE {
    return this._type;
  }

  set id(id: ID) {
    if (typeof id !== 'number') return;
    this._id = id;
  }

  get id(): ID {
    return this._id;
  }

  abstract clone(): this;
}
