from django.core.exceptions import ValidationError


def validate_amazing(value):
    must_be_in_item = set("превосходно", "роскошно")
    check_value = set(value.lower().split())

    difference = must_be_in_item - check_value

    if len(difference) == len(must_be_in_item):
        raise ValidationError(f"Обязательно нужно использовать {must_be_in_item}")

    return value


def validate_weight(value):
    if type(value) != int:
        raise ValidationError("Тип данных не int")
    if value <= 0 or value >= 32767:
        return ValidationError("Вес не находиться в диапазоне (0;32767)")
    return value

