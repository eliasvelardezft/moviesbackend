from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  username = models.CharField('username', max_length=50, primary_key=True)


  # Estos campos son los relacionados con que es un Usuario de django
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = [
    'first_name',
    'last_name'
  ]

  # manager
  objects = UserManager()

  def __str__(self):
    return f'{self.username} - {self.first_name} {self.last_name}'

