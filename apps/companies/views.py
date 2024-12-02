from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.companies.models import Companies
from apps.users.models import User
from utils.responseformat import success_response, fail_response


# Create your views here.
