from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "username": fields.Str(
        required=False
    ),
    "access_level": fields.Str(
        required=False
    )},
    location="query"
)
def get_groups(request, args):
    groups = Group.objects.all()

    # for param_name, param_value in args.items():
    #     groups = groups.filter(**{param_name: param_value})
    #
    # obj_filter = GroupsFilter(data=request.GET, queryset=groups)

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


def update_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm(
            instance=group
        )

    return render(request, 'groups/update.html', context={
            'form': form,
            'group': group,
            # 'students': group.students.all(),
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
