from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Movie, Rating
from drf_writable_nested.serializers import WritableNestedModelSerializer


class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = [
      'id',
      'rating',
      'comment',
      'user'
    ]

    
class MovieSerializer(WritableNestedModelSerializer):

  average_rating = serializers.ReadOnlyField(source='average')
  ratings = RatingSerializer(many=True, required=False)

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
      'user'
    ]

class MoviePagination(PageNumberPagination):
  page_size = 5
  page_size_query_param = 'page_size'
  max_page_size = 10

  
