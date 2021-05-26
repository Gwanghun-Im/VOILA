from django.db import models
from django.conf import settings


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField(blank=True)
    title = models.CharField(max_length=100,blank=True)
    vote_count = models.IntegerField(blank=True)
    vote_average = models.FloatField(blank=True)
    poster_path = models.TextField(blank=True,null=True)
    overview = models.TextField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies',blank=True)
    genre = models.ManyToManyField(Genre, related_name='movies',blank=True)

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    Review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
