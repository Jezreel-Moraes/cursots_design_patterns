import { CompositorProtocol } from './interfaces/CompositorProtocol';
import { LeafProtocol } from './interfaces/LeafProtocol';

export class Compositor implements CompositorProtocol {
  private children: LeafProtocol[] = [];

  add(...values: LeafProtocol[]): void {
    values.forEach((value) => this.children.push(value));
  }
  get price(): number {
    return this.children.reduce((sum, leaf) => sum + leaf.price, 0);
  }
}
