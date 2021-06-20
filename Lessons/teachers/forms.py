import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'position',
            'work_experience',
            'enroll_date',
            'graduate_date',
        ]

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
        if email and Teacher.objects.filter(email=email).exists():
            raise ValidationError('Sorry, the email already in use')
        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'position',
            'work_experience',
            'enroll_date',
            'graduate_date',
        ]
