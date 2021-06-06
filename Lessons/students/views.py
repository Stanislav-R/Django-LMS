from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from students.models import Student
from students.utils import format_records


def hello(request):
    return HttpResponse('Hello')


#
#
# @use_kwargs({
#     "count": fields.Int(
#         required=False,
#         missing=100,
#         validate=[validate.Range(min=1, max=999)]
#     )},
#     location="query"
# )
# def generate_students(request, count):
#     return HttpResponse('Hello')

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields


# @use_kwargs({
#     "first_name": fields.Str(
#         required=False,
#         missing='',
#         # validate=[validate.Range(min=1, max=999)]
#     )},
#     location="query"
# )
# def get_students(request, first_name):
#     qs = Student.objects.all()
#
#     students = qs.filter(first_name=first_name)
#
#     records = format_records(students)
#
#     return HttpResponse(records)
@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "birthdate": fields.Date(
        required=False
    )},
    location="query"
)
def get_students(request, args):

    students = Student.objects.all()

    for param_name, param_value in args.items():
        students = students.filter(**{param_name: param_value})

    records = format_records(students)

    return HttpResponse(records)
