import { Car } from './interfaces/car-protocol';

export class SmallCar extends Car {
  constructor() {
    super();
    this.type = 'SmallCar';
  }

  clone(): this {
    return cloneable.deepCopy(this);
  }
}

export class BigCar extends Car {
  constructor() {
    super();
    this.type = 'BigCar';
  }

  clone(): this {
    return cloneable.deepCopy(this);
  }
}

export class cloneable {
  public static deepCopy<T>(source: T): T {
    return Array.isArray(source)
      ? source.map((item) => this.deepCopy(item))
      : source instanceof Date
      ? new Date(source.getTime())
      : source && typeof source === 'object'
      ? Object.getOwnPropertyNames(source).reduce((o, prop) => {
          Object.defineProperty(
            o,
            prop,
            Object.getOwnPropertyDescriptor(source, prop)!,
          );
          o[prop] = this.deepCopy((source as { [key: string]: any })[prop]);
          return o;
        }, Object.create(Object.getPrototypeOf(source)))
      : (source as T);
  }
}
