from random import randint

from core.models import Person

from django.db import models


class Teacher(Person):
    work_experience = models.IntegerField(default=10)
    salary = models.PositiveIntegerField(default=1500)

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(1000, 3000)
        obj.save()
