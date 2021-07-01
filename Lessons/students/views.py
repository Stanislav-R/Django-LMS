from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student

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
    students = Student.objects.all().select_related('group', 'headed_group')

    # for param_name, param_value in args.items():
    #     if param_value:
    #         students = students.filter(**{param_name: param_value})

    obj_filter = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            # 'students': students,
            'obj_filter': obj_filter,
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
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'form': form
        }
    )


# @csrf_exempt
def update_student(request, id):  # noqa
    student = Student.objects.get(id=id)

    if request.method == 'GET':

        form = StudentUpdateForm(instance=student)

    elif request.method == 'POST':

        form = StudentUpdateForm(instance=student, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/update.html',
        context={
            'form': form
        }
    )


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'student': student
        }
    )
