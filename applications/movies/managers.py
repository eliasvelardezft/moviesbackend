from django.db import models
from django.contrib.auth.models import BaseUserManager
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authtoken.models import Token


class MovieManager(models.Manager):

    def ordered_by_date_desc(self):
        return self.model.objects.all().order_by('-release_date')
    
    def ordered_by_date_asc(self):
        return self.model.objects.all().order_by('release_date')
    
