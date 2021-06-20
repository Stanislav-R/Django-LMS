from django.core.management.base import BaseCommand

from students.models import Student


# HW 8-3
class Command(BaseCommand):
    help = 'Generating table of students.' # noqa

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of students to be created')

    def handle(self, *args, **options):
        return Student.generate_students(count=options['count'])
