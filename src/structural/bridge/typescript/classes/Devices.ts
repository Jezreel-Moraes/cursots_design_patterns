import { AbstractDevice } from './interfaces/AbstractDevice';

export class Radio extends AbstractDevice {
  protected _name = 'Radio';
}

export class TV extends AbstractDevice {
  protected _name = 'TV';
}
