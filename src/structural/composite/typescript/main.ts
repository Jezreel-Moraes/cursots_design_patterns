import { Compositor } from './classes/Compositor';
import { Leaf } from './classes/Leaf';

const compositor = new Compositor();
const leaf = new Leaf(10);
compositor.add(leaf, leaf, leaf, leaf);
console.log(leaf);
console.log(compositor);

console.log('leaf price: ', leaf.price);
console.log('compositor price: ', compositor.price);
