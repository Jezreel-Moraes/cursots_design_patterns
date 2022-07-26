import { User } from '../interfaces/user-protocol';

export default null;

class Database {
  private users: User[] = [];

  add(...users: User[]): void {
    users.forEach((user) => {
      this.users.push(user);
    });
  }

  remove(index: number): void {
    this.users.splice(index, 1);
  }

  show(): void {
    this.users.forEach((user) => console.log(user));
  }
}

export class DatabaseSingleton {
  private static _instance: Database | null = null;

  static create(): Database {
    if (!this._instance) this._instance = new Database();
    return this._instance;
  }
}
