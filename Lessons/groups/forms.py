from django.forms import ModelForm

import django_filters

from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['start_date']


class GroupUpdateForm(ModelForm):
    class Meta:
        fields = '__all__'


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['exact', 'icontains'],

        }
