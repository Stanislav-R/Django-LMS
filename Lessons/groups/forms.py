from django.core.exceptions import ValidationError
from django.forms import ModelForm

import django_filters

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = ['username', 'access_level', 'enroll_date', 'graduate_date']

    @staticmethod
    def normalize_username(value):
        return value.lower()

    def clean_username(self):
        username = self.cleaned_data['username']
        result = self.normalize_username(username)
        return result

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')


class GroupCreateForm(GroupBaseForm):
    pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        fields = ['username', 'access_level', 'enroll_date', 'graduate_date']


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'username': ['exact', 'icontains'],
            'access_level': ['exact', 'icontains'],

        }
