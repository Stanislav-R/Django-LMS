from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from students.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


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


@use_args(
    {
        "first_name": fields.Str(
            required=False
        ),
        "last_name": fields.Str(
            required=False
        ),
        "birthdate": fields.Date(required=False),
    },
    location="query",
)
def get_students(request, args):
    # Students = 42
    students = Student.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

    html_form = """
       <form method="get">
        <label >First name:</label>
        <input type="text" name="first_name"><br><br>

        <label >Last name:</label>
        <input type="text" name="last_name"><br><br>

        <label>Age:</label>
        <input type="number" name="age"><br><br>

        <input type="submit" value="Search">
       </form>
    """

    # records = format_records(students)
    # response = html_form + records
    #
    # return HttpResponse(response)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'abc': 42,
            'students': students
        }
    )


# @csrf_exempt  csrf token для проверки аутентификации
def create_student(request):
    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students_create'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'form': form
        }
    )


# @csrf_exempt
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'GET':

        form = StudentUpdateForm(instance=student)

    elif request.method == 'POST':

        form = StudentUpdateForm(instance=student, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students_update'))

    return render(
        request=request,
        template_name='students/update.html',
        context={
            'form': form
        }
    )
