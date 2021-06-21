from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateForm
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

    for param_name, param_value in args.items():
        groups = groups.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups
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
    group = Group.objects.get(id=id)

    if request.method == 'GET':

        form = GroupUpdateForm(instance=group)

    elif request.method == 'POST':

        form = GroupUpdateForm(instance=group, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'form': form
        }
    )
