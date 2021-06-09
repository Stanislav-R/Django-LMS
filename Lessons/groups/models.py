import random
from django.db import models
from faker import Faker


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

    # def __str__(self):
    #     return self.username

    def __str__(self):
        return f'{self.username}, {self.access_level}'

    @staticmethod
    def generate_groups(count):
        faker = Faker()
        for _ in range(count):
            gp = Group(
                username=faker.first_name().lower(),
                access_level=random.choice(Group.CHOICES)[1]

            )

            gp.save()
