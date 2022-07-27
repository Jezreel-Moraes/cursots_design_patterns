import { UserProtocol } from '../interfaces/UserProtocol';

const users: UserProtocol[] = [];

export const DatabaseModule = {
  add(user: UserProtocol): void {
    users.push(user);
  },

  remove(index: number): void {
    users.splice(index, 1);
  },

  show(): void {
    users.forEach((user) => console.log(' ', user));
  },
};
