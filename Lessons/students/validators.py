import datetime

from django.core.exceptions import ValidationError


def adult_validator(birthdate):
    ADULT_AGE_LIMIT = 18

    age = datetime.datetime.now().year - birthdate.year

    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')


# HW 9-4 with '*'
def validate_domain_email(email):
    DOMAIN_WHITE_LIST = [
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'ukr.net', 'i.ua'
    ]
    # if sum(1 for domain in DOMAIN_WHITE_LIST if domain not in email) > 0:
    count = len(DOMAIN_WHITE_LIST)
    for domain in DOMAIN_WHITE_LIST:
        if domain not in email:
            count -= 1
    if count <= 0:
        raise ValidationError('Sorry, the email is invalid')
    return email
