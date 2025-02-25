import re

from django.core.exceptions import ValidationError


def validate_amazing(value):
    must_be_in_item = {'превосходно', 'роскошно'}
    check_value = set(re.sub(r'[^\s\w]', ' ', value.lower()).split())

    difference = must_be_in_item - check_value

    if len(difference) == len(must_be_in_item):
        raise ValidationError(f'Обязательно нужно использовать '
                              f'{" или ".join(must_be_in_item)}')

    return value


def validate_weight(value):
    if type(value) is not int:
        raise ValidationError('Тип данных не int')
    if value <= 0 or value >= 32767:
        raise ValidationError('Вес не находиться в диапазоне (0;32767)')
    return value


def validate_must_be_param(*args):
    def validate_must(value):
        must_be_in_item = set(args)
        check_value = set(re.sub(r'[^\s\w]', ' ', value.lower()).split())
        difference = must_be_in_item - check_value

        if len(difference) == len(must_be_in_item):
            raise ValidationError(f'Обязательно нужно использовать '
                                  f'{" или ".join(must_be_in_item)}')

        return value
    return validate_must
