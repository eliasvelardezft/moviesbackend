import json
from django.urls import reverse
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from .models import Movie, Rating


# Create your tests here.


class MoviesTestCase(APITestCase):
  
  def test_create_movie(self):
    expectedResponse = {
        "id": 1,
        "title": "Spotlight",
        "release_date": "2017-06-14",
        "genre": "Thriller",
        "plot": "unos periodistas etc",
        "ratings": []
    }
    data = {
      "title": "Spotlight",
      "release_date": "2017-06-14",
      "genre": "Thriller",
      "plot": "unos periodistas etc"
    }
    response = self.client.post("/movies/movies/", data, format="json")
    assert response.data == expectedResponse

