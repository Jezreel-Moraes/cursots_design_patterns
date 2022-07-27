import { AdminUser } from './AdminUser';
import { UserAddressProtocol } from './interfaces/UserAddressProtocol';
import { UserProtocol } from './interfaces/UserProtocol';

export class UserProxy extends UserProtocol {
  private realUser: AdminUser | null = null;
  private realUserAddress: UserAddressProtocol[] | null = null;

  private createUser(): AdminUser {
    return new AdminUser(this.firstName, this.userName);
  }

  async getAddresses(): Promise<UserAddressProtocol[]> {
    if (!this.realUser) this.realUser = this.createUser();
    if (!this.realUserAddress)
      this.realUserAddress = await this.realUser.getAddresses();

    return this.realUserAddress;
  }
}
