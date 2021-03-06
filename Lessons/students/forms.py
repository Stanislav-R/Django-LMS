import re

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

import django_filters

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'age',
            'birthdate',
            'enroll_date',
            'graduate_date',
        ]

        widgets = {'birthdate': DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        return '+' + re.sub("\D", "", value) # noqa

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Student.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError('Sorry, the email already in use')
        return email


class StudentCreateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'enroll_date',
            'graduate_date',
        ]


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = '__all__'


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
            'age': ['lt', 'gt'],
        }
