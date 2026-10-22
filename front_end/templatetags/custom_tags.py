import random
from datetime import timedelta, datetime

import time
from django import template
from dateutil import parser
import pytz

register = template.Library()


# THis filter checks if it's currently BST and adds 1 hour to the beggining time if it is
@register.filter(name='to_date')
def to_date(value):
    # Parse the input string into a datetime object
    date_time = parser.isoparse(value)

    # Determine the timezone for British time (including BST)

    british_timezone = pytz.timezone('Europe/London')
    uk_datetime = date_time.astimezone(british_timezone)
    print(date_time)
    print(uk_datetime)
    return uk_datetime


@register.filter
def is_number(value, number):
    return value == number


@register.simple_tag
def random_int(start, end):
    return random.randint(start, end)
