""" Test for the user API """

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrip.auth import get_user_model


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
  
