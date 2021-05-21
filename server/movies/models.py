from django.db import models
from django.conf import settings


# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    poster_path = models.TextField()
    overview = models.TextField(blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=20)
    movie = models.ManyToManyField(Movie, related_name='genres',blank=True)
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):
    Review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
