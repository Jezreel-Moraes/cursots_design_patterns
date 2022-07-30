import { DeviceProtocol } from './interfaces/DeviceProtocol';
import { RemoteControlProtocol } from './interfaces/RemoteControlProtocol';

export class RemoteControl implements RemoteControlProtocol {
  constructor(protected device: DeviceProtocol) {}

  get devicePower(): boolean {
    return this.device.power;
  }
  get deviceVolume(): number {
    return this.device.volume;
  }
  get deviceName(): string {
    return this.device.name;
  }

  togglePower(): void {
    this.device.power = !this.device.power;
  }
}
