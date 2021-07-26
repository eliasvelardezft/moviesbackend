from django.db import models
from django.contrib.auth.models import BaseUserManager
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager, models.Manager):

  def _create_user(self, first_name, last_name, username, movies_watchlist, password, is_staff, is_superuser, **extra_fields):
    user = self.model(
      first_name = f'{first_name[0].upper()}{first_name[1:]}',
      last_name = f'{last_name[0].upper()}{last_name[1:]}',
      username = username,
      is_staff = is_staff,
      is_superuser = is_superuser,

      **extra_fields
    )
    user.movies_watchlist.set(movies_watchlist)
    user.set_password(password)

    user.save(using=self.db)
    Token.objects.get_or_create(user=user)
    return user
  
  def create_user(self, first_name, last_name, username, movies_watchlist=[], password=None, **extra_fields):
    return self._create_user(first_name, last_name, username, movies_watchlist, password, False, False, **extra_fields)

  def create_superuser(self, first_name, last_name, username, movies_watchlist=[], password=None, **extra_fields):
    return self._create_user(first_name, last_name, username, movies_watchlist, password, True, True, **extra_fields)  
  


