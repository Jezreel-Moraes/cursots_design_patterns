export const emailValidate = (email: string): boolean => {
  if (email.indexOf('@') === -1) return false;
  if (email.indexOf('.') === -1) return false;
  return true;
};
