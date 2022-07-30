from classes.interfaces.validations_protocol import ValidationsProtocol
from outside_code_validate_email import is_email


class Validations(ValidationsProtocol):

    @staticmethod
    def is_email(email: str):
        return is_email(email)
