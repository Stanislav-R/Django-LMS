import datetime

from django.core.exceptions import ValidationError


def adult_validator(birthdate, adult_age_limit=18):

    age = datetime.datetime.now().year - birthdate.year

    if age < adult_age_limit:
        raise ValidationError(f'Age should be greater than {adult_age_limit} y.o.')


class AdultValidator:

    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, birthdate):
        adult_validator(birthdate, self.age_limit)


# HW 9-4 with '*'
def validate_domain_email(email):
    DOMAIN_WHITE_LIST = [  # noqa
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'ukr.net', 'i.ua'
    ]
    # if sum(1 for domain in domain_white_list if domain not in email) > 0:
    count = len(DOMAIN_WHITE_LIST)
    for domain in DOMAIN_WHITE_LIST:
        if domain not in email:
            count -= 1
    if count <= 0:
        raise ValidationError('Sorry, the email is invalid')
    return email
