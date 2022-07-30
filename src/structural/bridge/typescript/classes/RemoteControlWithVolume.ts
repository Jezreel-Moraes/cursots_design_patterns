import { RemoteControl } from './RemoteControl';

export class RemoteControlWithVolume extends RemoteControl {
  volumeUp(): void {
    const volume = this.device.volume;
    this.device.volume = volume >= 100 ? volume : volume + 10;
  }
  volumeDown(): void {
    const volume = this.device.volume;
    this.device.volume = volume <= 0 ? volume : volume - 10;
  }
}
