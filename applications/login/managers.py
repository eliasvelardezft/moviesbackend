from django.db import models
from django.contrib.auth.models import BaseUserManager
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager, models.Manager):

  def username_exists(self, username):
    result = self.model.objects.filter(
      username = username
    )
    if len(result) > 0:
      return True
    else:
      return False

  def _create_user(self, first_name, last_name, username, password, is_staff, is_superuser, **extra_fields):
    user = self.model(
      first_name = f'{first_name[0].upper()}{first_name[1:]}',
      last_name = f'{last_name[0].upper()}{last_name[1:]}',
      username = username,
      is_staff = is_staff,
      is_superuser = is_superuser,
      **extra_fields
    )
    user.set_password(password)

    if self.username_exists(user.username):
      return Response({"error": "ya existe el username"})
    else:
      user.save(using=self.db)
      Token.objects.get_or_create(user=user)
      return user
  
  def create_user(self, first_name, last_name, username, password=None, **extra_fields):
    return self._create_user(first_name, last_name, username, password, False, False, **extra_fields)

  def create_superuser(self, first_name, last_name, username, password=None, **extra_fields):
    return self._create_user(first_name, last_name, username, password, True, True, **extra_fields)  
  


