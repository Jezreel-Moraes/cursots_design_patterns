export interface RemoteControlProtocol {
  togglePower(): void;
  get devicePower(): boolean;
  get deviceVolume(): number;
  get deviceName(): string;
}
