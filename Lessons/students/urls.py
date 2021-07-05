from django.urls import path

from students.views import create_student, delete_student, get_students, UpdateStudentView, StudentUpdateView

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    # path('update/<int:id>/', update_student, name='update'),
    # path('update/<int:pk>/', UpdateStudentView.update_object, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
