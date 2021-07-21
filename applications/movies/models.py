from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import SET_NULL
from .managers import MovieManager
from applications.login.models import User
# Create your models here.


class Rating(models.Model):

    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)


class Movie(models.Model):

    title = models.CharField(max_length=150)
    release_date = models.DateField()
    genre = models.CharField(max_length=20)
    plot = models.TextField()
    ratings = models.ManyToManyField(Rating, blank=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def _get_average_rating(self):
        sum = 0
        ratings = self.ratings.all()
        if(self.ratings.count() == 0):
            return 0.0
        
        for r in ratings:                
            sum += r.rating

        return sum/len(ratings)

        
    average = property(_get_average_rating)

    objects = MovieManager()

    def __str__(self):
        return f'{self.title} - {self.genre}'



    