from exceptions import (
    EmptyInputError,
    NotDigitError,
    InvalidLengthError,
    OutOfRangeError,
    DuplicateNumberError,
    InvalidInputError,
)


def validate_numbers(raw: str) -> list[int]:
    if not raw.strip():
        raise EmptyInputError("입력값이 없습니다.")

    if not raw.strip().isdigit():
        raise NotDigitError("숫자만 입력해야 합니다.")

    digits = [int(d) for d in raw.strip()]

    if len(digits) != 3:
        raise InvalidLengthError("숫자는 3개여야 합니다.")

    if any(d == 0 for d in digits):
        raise OutOfRangeError("1~9 사이의 숫자만 입력 가능합니다.")

    if len(set(digits)) != 3:
        raise DuplicateNumberError("중복된 숫자는 입력할 수 없습니다.")

    return digits


def validate_retry_command(raw: str) -> str:
    if raw.strip() not in ("1", "2"):
        raise InvalidInputError("1 또는 2를 입력해주세요.")
    return raw.strip()
