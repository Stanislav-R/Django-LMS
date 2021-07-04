from django.forms import DateInput, ModelForm

from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['start_date']

        widgets = {'end_date': DateInput(attrs={'type': 'date'})}
