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

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


  @action(methods=['GET'], detail=False)
  def get_movies_ascending_date(self, *args, **kwargs):
    queryset = Movie.objects.ordered_by_date_asc();
    serializer = MovieSerializer(queryset, many=True);
    return Response(serializer.data)
  
  @action(methods=['GET'], detail=False)
  def get_movies_descending_date(self, *args, **kwargs):
    queryset = Movie.objects.ordered_by_date_desc();
    serializer = MovieSerializer(queryset, many=True);
    return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  queryset = Rating.objects.all()
  authentication_classes = [TokenAuthentication]
  permission_classes = [AllowAny]