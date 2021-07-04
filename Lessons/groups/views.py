from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import GroupCreateForm
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all()

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups,
        }
    )


def create_group(request):
    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'form': form
        }
    )


def update_group(request, id): # noqa
    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups:list'))

    else:
        form = GroupCreateForm(instance=group)

    return render(request, 'groups/update.html', context={
            'form': form,
            'group': group,
            'students': group.students.select_related('headed_group').all()
        }
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={
            'group': group
        }
    )
