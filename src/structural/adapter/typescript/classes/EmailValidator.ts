import { emailValidate } from '../outside-code/emailValidator';

export class EmailValidator {
  static validate(email: string): boolean {
    return emailValidate(email);
  }
}
