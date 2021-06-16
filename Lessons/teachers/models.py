import datetime

from django.db import models


# HW 7-3
# Create your models here.
from students.validators import validate_domain_email


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(
        max_length=50, null=True, validators=[validate_domain_email]
    )
    position = models.CharField(max_length=70, null=False)
    work_experience = models.IntegerField(default=10)
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.full_name()}, {self.position}, {self.work_experience}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'
