from django.db import models
from django.db.models import Q
from django.db.models import Avg
from django.db.models.functions import Coalesce



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
        return self.model.objects.all().annotate(avg_rating=Avg(Coalesce('ratings__rating', 0))).order_by(order[sortingParam])


