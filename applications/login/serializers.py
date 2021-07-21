from applications.movies.serializers import MovieSerializer
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from applications.movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'password',
      'movies_watchlist'
    ]
  
  def __init__(self, *args, **kwargs):
    super(UserSerializer, self).__init__(*args, **kwargs)
    try:
      if self.context['request'].method in ['POST', 'PATCH']:
        self.fields['movies_watchlist'] = serializers.PrimaryKeyRelatedField(
          many=True,
          queryset=Movie.objects.all(), 
          required=False
        )
      else:
        self.fields['movies_watchlist'] = MovieSerializer(many=True, required=False)
    except KeyError:
      pass
    
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=50, allow_blank=True)
  password = serializers.CharField(
    label=_('Password'),
    style= {'input_type': 'password'},
    max_length = 50,
    write_only = True,
    allow_blank=True
  )

  def validate(self, data):
    username = data.get('username')
    password = data.get('password')
    if username and password:
      user = authenticate(username=username, password=password)
      if not user:
        msg = _('Incorrect credentials')
        raise serializers.ValidationError(msg, code='authorization')
    else:
      msg = _('Incomplete credentials')
      raise serializers.ValidationError(msg, code='authorization')

    data['user'] = user
    return data