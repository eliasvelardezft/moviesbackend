from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import MovieManager
# Create your models here.


class Rating(models.Model):

    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    comment = models.TextField()


class Movie(models.Model):

    title = models.CharField(max_length=150)
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=20)
    plot = models.TextField()
    ratings = models.ManyToManyField(Rating, blank=True)

    objects = MovieManager()

    def __str__(self):
        return f'{self.title} - {self.genre}'

    