import datetime

from django.db import models

from teachers.models import Teacher

# from students.models import Student


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        # Student,
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )

    teachers = models.ManyToManyField(
        to=Teacher,
        related_name='groups'
    )

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
