from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


class CheckBirthDate:
    def __init__(self, age=0):
        self.age = age

    def __call__(self, value):
        diff = relativedelta(date.today(), value).years
        if diff < self.age:
            raise ValidationError(f"Запрещена регистрация пользователей младше {self.age} лет")
