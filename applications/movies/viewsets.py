from django.db.models.query import QuerySet
from applications.movies.apps import MoviesConfig
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework import status

from rest_framework.authtoken.models import Token
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()
  authentication_classes = [TokenAuthentication]
  permission_classes = [AllowAny]

  def get_queryset(self):
      qs = {
        'ascDate': Movie.objects.ordered_by_date('asc'),
        'descDate': Movie.objects.ordered_by_date('desc'),
        'ascRating': Movie.objects.ordered_by_avg_rating('asc'),
        'descRating': Movie.objects.ordered_by_avg_rating('desc')
      }
      queryset = Movie.objects.all()
      filter = self.request.META.get('HTTP_SEARCHSORT')
      if filter in qs.keys():
        queryset = qs[f'{filter}']
      return queryset



class RatingViewSet(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  queryset = Rating.objects.all()
  authentication_classes = [TokenAuthentication]
  permission_classes = [AllowAny]