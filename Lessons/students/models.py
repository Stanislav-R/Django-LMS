import datetime

from core.models import Person

from django.db import models

from groups.models import Group


class Student(Person):
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}, {self.group}'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.save()
