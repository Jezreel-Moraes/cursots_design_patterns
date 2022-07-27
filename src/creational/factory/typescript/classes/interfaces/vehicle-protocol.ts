export abstract class Vehicle {
  constructor(public name: string) {}

  pickUp(customerName: string): void {
    console.log(`${this.name} is looking for ${customerName}`);
  }

  stop(): void {
    console.log(`${this.name} stopped`);
  }
}
