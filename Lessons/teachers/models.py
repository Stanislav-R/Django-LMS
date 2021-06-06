from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    position = models.CharField(max_length=70, null=False)
    work_experience = models.IntegerField(default=10)
