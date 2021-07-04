from courses.models import Course


from django.forms import DateInput, ModelForm


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['start_date']

        widgets = {'end_date': DateInput(attrs={'type': 'date'})}
