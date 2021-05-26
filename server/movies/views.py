
from django.db.models.deletion import PROTECT
from django.http.response import JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Genre, Movie, Review, Comment
from .serializers import MovieListSerializer, ReviewSerializer, CommentSerializer,MovieSerializer,GenreSerializer

import requests
api_key = '3a5a5d5bd9ebc60efe15703f924c7578'

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

def findUser(request):
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(get_user_model(), email=payload["email"])
    return user

@api_view(['GET'])
def getMovie(request):
    movies = Movie.objects.all()
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=ko-kr'
    req = requests.get(url)
    for movie in req.json().get('results'):
        try:
            Movie.objects.get(id=movie.get('id'))
        except:
            serializer = MovieListSerializer(data=movie)
            if serializer.is_valid(raise_exception=True):
                serializer.save(genre=[movie.get('genre_ids')])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        movie = get_object_or_404(Movie, pk=pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, user=findUser(request))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST','GET', 'DELETE', 'PUT'])
def review(request, pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete':f'리뷰 {review_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(Review = review, user=findUser(request))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def like_movie(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = findUser(request)
    state = 0
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
    else:
        state = 1
        movie.like_users.add(user)
    print(state)
    return Response(state)

@api_view(['POST'])
def like_review(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = findUser(request)
    state = 0
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
    else:
        state = 1
        review.like_users.add(user)
    return Response(state)

@api_view(['GET','DELETE'])
def comment(request, pk, review_pk, comment_pk):
    review = get_object_or_404(Review, movie=pk, pk=review_pk)
    comment = get_object_or_404(Comment, Review=review, pk= comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete':f'리뷰 {review_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search(request,title):
    movies = Movie.objects.all()
    url = f'https://api.themoviedb.org/3/search/movie/?api_key={api_key}&language=ko-kr&query={title}'
    req = requests.get(url)
    for movie in req.json().get('results'):
        try:
            Movie.objects.get(id=movie.get('id'))
        except:
            serializer = MovieListSerializer(data=movie)
            serializer.genres = [movie.get('genre_ids')]
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    return Response(req.json().get('results'))

@api_view(['GET'])
def detail(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=ko-kr'
    movie = requests.get(url).json()
    try:
        Movie.objects.get(id=movie.get('id'))
    except:
        serializer = MovieListSerializer(data=movie)
        serializer.genres = [movie.get('genre_ids')]
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    title = movie.get('title')
    youtube_url = f'https://www.googleapis.com/youtube/v3/search?key=AIzaSyBh8RRzXwFyUKx5KXL4X8bXf_JH16T5eVA&part=snippet&type=video&q={title}+officail+trailer'
    youtube = requests.get(youtube_url).json()
    data={
        'movie':movie,
        'youtube':youtube
    }

    return Response(data)


from collections import Counter

@api_view(['GET'])
def word(request, user_pk):
    user = findUser(request)
    movie = user.like_movies.all()
    words = ''
    for i in movie:
        words += i.overview
    words = words.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
    wC = Counter(words.split())
    data = [{'text':k, 'value':v} for k,v in wC.items()]
    return Response(data)