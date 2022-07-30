from classes.interfaces.validate_component_protocol import \
    ValidationComponentProtocol


class ValidateEmail(ValidationComponentProtocol):
    def validate(self, value) -> bool:
        try:
            return '@' in value
        except TypeError as error:
            error = error
            return False


class ValidateString(ValidationComponentProtocol):
    def validate(self, value) -> bool:
        return isinstance(value, str)


class ValidateInt(ValidationComponentProtocol):
    def validate(self, value) -> bool:
        return isinstance(value, int)


class ValidateCompositor(ValidationComponentProtocol):
    def __init__(self) -> None:
        self.children: list[ValidationComponentProtocol] = []

    def add(self, *args: ValidationComponentProtocol):
        for item in args:
            self.children.append(item)

    def validate(self, value) -> bool:
        valid = True
        for validator in self.children:
            if not validator.validate(value):
                print(f'{validator.__class__.__name__}: Fail')
                valid = False
            else:
                print(f'{validator.__class__.__name__}: Passed')
        return valid
