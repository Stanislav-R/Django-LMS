from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Group

from students.utils import format_records

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

    records = format_records(groups)

    return HttpResponse(records)


@csrf_exempt
def create_group(request):
    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    """

    response = html_form

    return HttpResponse(response)
