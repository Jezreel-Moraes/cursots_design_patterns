import { EmailValidator } from './classes/EmailValidator';

const email = 'email@gmail.com';
console.log(email, 'is email:', EmailValidator.validate(email));
