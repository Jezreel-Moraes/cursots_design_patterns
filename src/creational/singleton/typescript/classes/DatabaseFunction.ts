import { UserProtocol } from '../interfaces/UserProtocol';

export const DatabaseFunction = (function () {
  const users: UserProtocol[] = [];

  return {
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
})();
