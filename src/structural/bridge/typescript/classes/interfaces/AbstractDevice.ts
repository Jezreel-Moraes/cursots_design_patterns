import { DeviceProtocol } from './DeviceProtocol';

export abstract class AbstractDevice implements DeviceProtocol {
  protected powerStatus = false;
  protected volumeStatus = 10;
  protected _name = 'AbstractDevice';

  get power(): boolean {
    return this.powerStatus;
  }
  set power(powerStatus: boolean) {
    this.powerStatus = powerStatus;
  }
  get volume(): number {
    return this.volumeStatus;
  }
  set volume(volume: number) {
    this.volumeStatus = volume;
  }
  get name(): string {
    return this._name;
  }
}
