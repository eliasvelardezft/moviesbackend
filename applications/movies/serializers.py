from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = [
      'id',
      'rating',
      'comment',
    ]

    
class MovieSerializer(serializers.ModelSerializer):
  
  ratings = RatingSerializer(many=True)

  class Meta:
    model = Movie
    fields = [
      'id',
      'title',
      'release_date',
      'genre',
      'plot',
      'ratings',
    ]


