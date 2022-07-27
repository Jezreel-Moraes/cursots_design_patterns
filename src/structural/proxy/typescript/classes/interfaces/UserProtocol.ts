import { UserAddressProtocol } from './UserAddressProtocol';

export abstract class UserProtocol {
  constructor(public firstName: string, public userName: string) {}

  abstract getAddresses(): Promise<UserAddressProtocol[]>;
}
