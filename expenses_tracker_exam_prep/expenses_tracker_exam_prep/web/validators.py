from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ONLY_LETTERS_VALIDATOR_EXCEPTION_MESSAGE = 'Ensure this value contains only letters.'


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max size is {self.max_size:.2f} MB'


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError(ONLY_LETTERS_VALIDATOR_EXCEPTION_MESSAGE)
