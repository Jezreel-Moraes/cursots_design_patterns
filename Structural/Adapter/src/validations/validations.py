from .outside_code_validate_email import is_email
from .validations_interface import ValidationsInterface

class Validations(ValidationsInterface):
   
   @staticmethod
   def is_email(email: str):
      return is_email(email)
      