import { LeafProtocol } from './LeafProtocol';

export interface CompositorProtocol extends LeafProtocol {
  add(...values: CompositorProtocol[]): void;
}
