from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher


# def get_teachers(request):
#     teachers = Teacher.objects.all()
#
#     obj_filter = TeachersFilter(data=request.GET, queryset=teachers)
#
#     return render(
#         request=request,
#         template_name='teachers/list.html',
#         context={
#             'obj_filter': obj_filter,
#         }
#     )
#
#
# def create_teacher(request):
#     if request.method == 'POST':
#         form = TeacherCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#
#     else:
#         form = TeacherCreateForm()
#
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={
#             'form': form
#         }
#     )
#
#
# def update_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#
#     if request.method == 'POST':
#         form = TeacherUpdateForm(request.POST, instance=teacher)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#
#     else:
#         form = TeacherUpdateForm(instance=teacher)
#
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={
#             'form': form
#         }
#     )
#
#
# def delete_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:list'))
#
#     return render(
#         request=request,
#         template_name='teachers/delete.html',
#         context={
#             'teacher': teacher
#         }
#     )


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'obj_filter'

    def get(self, request, *args, **kwargs):
        obj_filter = TeachersFilter
        context = {
            'obj_filter': obj_filter,
        }
        return render(request, 'teachers/list.html', context)


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
