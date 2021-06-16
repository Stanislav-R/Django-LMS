import datetime

from django.core.exceptions import ValidationError


def adult_validator(birthdate):
    ADULT_AGE_LIMIT = 18

    age = datetime.datetime.now().year - birthdate.year

    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')


# HW 9-4 with '*'
def validate_domain_email(email):
    domain_white_list = [
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'ukr.net', 'i.ua'
    ]
    count = len(domain_white_list)
    for domain in domain_white_list:
        if domain not in email:
            count -= 1
    if count <= 0:
        raise ValidationError('Sorry, the email is invalid')
    return email
