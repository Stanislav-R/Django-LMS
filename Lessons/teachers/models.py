from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50, null=False)
    position = models.CharField(max_length=70, null=False)
    work_experience = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.full_name()}, {self.position}, {self.work_experience}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'
