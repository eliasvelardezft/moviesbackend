import json
from django.urls import reverse
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from .models import User

class LoginTestCase(APITestCase):

  def test_login(self):
    user = User.objects.create_user('Lionel', 'Messi', 'lmessi', 'lmessi')
    token, created = Token.objects.get_or_create(user=user)
    expectedResponse = {
      'user': {
        'username': 'lmessi'
      },
      'token': f'{token}'
    }
    data = {
      "username": "lmessi",
      "password": "lmessi"
    }
    response = self.client.post('/login/users/login/', data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expectedResponse
  
  def test_create_user(self):
    expectedResponse = {
      'code': 'ok'
    }
    data = {
      'first_name': 'Elias',
      'last_name': 'Velardez',
      'username': 'eliasvelardez',
      'password': 'eliasvelardez'
    }
    response = self.client.post('/login/users/', data, format='json')
    assert response.data == expectedResponse
    
    