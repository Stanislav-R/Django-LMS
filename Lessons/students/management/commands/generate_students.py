from django.core.management.base import BaseCommand
from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generating table of students.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of students to be created')

    def handle(self, *args, **options):
        count = options['count']
        faker = Faker()
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_between(start_date='-65y', end_date='-18y')
            )

            st.save()
