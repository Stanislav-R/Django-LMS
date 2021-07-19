import re

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

import django_filters

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'age',
            'birthdate',
            'work_experience',
            'salary',
        ]
        widgets = {'birthdate': DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        return '+' + re.sub("\D", "", value)  # noqa
        # return '+' + ''.join(i for i in value if i.isdigit())

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Teacher.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError('Sorry, the email already in use')
        return email


class TeacherCreateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'work_experience',
            'salary',
        ]


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        fields = '__all__'


class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
            'salary': ['lt', 'gt'],
        }
