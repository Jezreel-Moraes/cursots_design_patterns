export interface DeviceProtocol {
  get power(): boolean;
  set power(powerStatus: boolean);
  get volume(): number;
  set volume(volume: number);
  get name(): string;
}
