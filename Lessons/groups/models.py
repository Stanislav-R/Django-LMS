import datetime
import random

from django.db import models

from faker import Faker


# HW 7-2
# Create your models here.

class Group(models.Model):
    username = models.CharField(max_length=30, null=False)
    # Choose access level
    CHOICES = (
        ('Tr', 'Traverse Folder'),
        ('RW', 'Read and Write'),
        ('FA', 'Full Access'),
    )
    access_level = models.CharField(max_length=60, choices=CHOICES)
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.username}, {self.access_level}'

    @staticmethod  # HW 8-1
    def generate_groups(count):
        faker = Faker()
        for _ in range(count):
            gp = Group(
                username=faker.first_name().lower(),
                access_level=random.choice(Group.CHOICES)[1]

            )

            gp.save()
