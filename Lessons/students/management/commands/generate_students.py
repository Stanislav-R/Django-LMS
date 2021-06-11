from django.core.management.base import BaseCommand
from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generating table of students.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of students to be created')

    def handle(self, *args, **options):
        return Student.generate_students(count=options['count'])
