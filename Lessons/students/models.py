import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from faker import Faker

from groups.models import Group
from students.validators import AdultValidator, validate_domain_email


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(
        max_length=80, null=False, validators=[MinLengthValidator(2)]
    )
    phone_number = models.CharField(max_length=15, null=True)
    age = models.IntegerField(default=42)
    email = models.EmailField(
        max_length=50, null=True, validators=[validate_domain_email]
    )
    birthdate = models.DateField(
        # default=datetime.date.today, validators=[adult_validator]
        # default=datetime.date.today, validators=[AdultValidator(21)]
    )
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}, {self.group}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y')
            )

            st.age = relativedelta(datetime.date.today(), st.birthdate).years

            st.save()
