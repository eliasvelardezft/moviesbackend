from django.db import models
from django.contrib.auth.models import BaseUserManager
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.db.models import Avg, Sum


class MovieManager(models.Manager):

    def ordered_by_date(self, sortingParam):
        order = {
            'asc': 'release_date',
            'desc': '-release_date'
        }
        return self.model.objects.all().order_by(f'{order[sortingParam]}')

    def ordered_by_avg_rating(self, sortingParam):
        order = {
            'asc': 'avg_rating',
            'desc': '-avg_rating'
        }
        return self.model.objects.annotate(avg_rating=Avg('ratings__rating')).order_by(f'{order[sortingParam]}')


