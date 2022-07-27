import { UserAddressProtocol } from './interfaces/UserAddressProtocol';
import { UserProtocol } from './interfaces/UserProtocol';
import { UserAddress } from './UserAddress';

export class AdminUser extends UserProtocol {
  async getAddresses(): Promise<UserAddressProtocol[]> {
    await new Promise((resolve) => setTimeout(resolve, 2000));
    return [new UserAddress('Street 1', 1), new UserAddress('Street 2', 2)];
  }
}
