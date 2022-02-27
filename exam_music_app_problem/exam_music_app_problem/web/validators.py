import re

from django.core.exceptions import ValidationError

ONLY_LETTERS_NUMBERS_UNDERSCORE_VALIDATOR_EXCEPTION_MESSAGE = \
    "Ensure this value contains only letters, numbers, and underscore."


def only_letters_numbers_underscore_validator(value):
    if not re.match("^[A-Za-z0-9_]*$", value):
        raise ValidationError(ONLY_LETTERS_NUMBERS_UNDERSCORE_VALIDATOR_EXCEPTION_MESSAGE)
