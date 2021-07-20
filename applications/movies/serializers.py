from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
import json
from drf_writable_nested.serializers import WritableNestedModelSerializer


class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = [
      'id',
      'rating',
      'comment',
    ]

    
class MovieSerializer(WritableNestedModelSerializer):

  average_rating = serializers.ReadOnlyField(source='average')


  class Meta:
    model = Movie
    fields = [
      'id',
      'title',
      'release_date',
      'genre',
      'average_rating',
      'plot',
      'ratings',
    ]

  def __init__(self, *args, **kwargs):
    super(MovieSerializer, self).__init__(*args, **kwargs)
    try:
      if self.context['request'].method in ['PUT']:
        self.fields['ratings'] = serializers.PrimaryKeyRelatedField(
          many=True,
          queryset=Rating.objects.all(), 
          required=False
        )
      else:
        self.fields['ratings'] = RatingSerializer(many=True, required=False);
    except KeyError:
      pass
  

{
    "ratings": [
        {
            "rating": 10,
            "comment": "muy bue"
        },
        {
            "rating": 9,
            "comment": "casi perfecto"
        }
    ]
}
  
