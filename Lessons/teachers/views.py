from django.http import HttpResponse

# Create your views here.
from webargs import fields
from webargs.djangoparser import use_args

from students.utils import format_records
from teachers.models import Teacher


@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "position": fields.Str(
        required=False
    ),
    "work_experience": fields.Int(
        required=False
    )},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})

    records = format_records(teachers)

    return HttpResponse(records)