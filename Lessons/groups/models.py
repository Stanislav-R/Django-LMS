from django.db import models


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
