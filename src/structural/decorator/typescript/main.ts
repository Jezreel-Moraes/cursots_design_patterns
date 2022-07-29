import { PrintedTShirtDecorator } from './classes/PrintedTshirtDecorator';
import { TShirt } from './classes/TShirt';

const tshirt = new TShirt();
console.log(tshirt.price, tshirt.name);

const printedTShirt = new PrintedTShirtDecorator(tshirt);
console.log(printedTShirt.price, printedTShirt.name);

const rePrintedTShirt = new PrintedTShirtDecorator(printedTShirt);
console.log(rePrintedTShirt.price, rePrintedTShirt.name);
