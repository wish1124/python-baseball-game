class InvalidInputError(ValueError):
    pass


class EmptyInputError(InvalidInputError):
    pass


class NotDigitError(InvalidInputError):
    pass


class InvalidLengthError(InvalidInputError):
    pass


class OutOfRangeError(InvalidInputError):
    pass


class DuplicateNumberError(InvalidInputError):
    pass
