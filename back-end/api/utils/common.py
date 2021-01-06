import csv
import base64
import os
import datetime

from django.http import HttpResponse
from django.utils import timezone
from .constants import AUTH_TOKEN_EXPIRES_HOURS

def produce_csv_response(data):
    # data: list of lists

    csv_response = HttpResponse(content_type='text.csv')
    csv_response['Content-Disposition'] = 'attachment; filename="out.csv"'
    writer = csv.writer(csv_response)
    writer.writerows(data)

    return csv_response

def create_auth_token():
    return base64.b64encode(os.urandom(64))

def token_expires_delta(past=True, hours=None):
    if not hours:
        hours = AUTH_TOKEN_EXPIRES_HOURS
    return datetime.timedelta(hours=hours)

def to_bytes(input):
    return bytes(input, 'utf-8')

def get_now():
    return timezone.now()