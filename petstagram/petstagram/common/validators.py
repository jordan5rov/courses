from django.core.exceptions import ValidationError


def validate_only_letters(value):
    # for ch in value:
    #     if not ch.isalpha():
    #         # Invalid case
    #         raise ValidationError('Value must contain only letters!')
    # valid case
    if not all(ch.isalpha for ch in value):
        raise ValidationError('Value must contain only letters!')


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        file_size = value.file.size
        if file_size > max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {str(max_size)}')
    return validate
