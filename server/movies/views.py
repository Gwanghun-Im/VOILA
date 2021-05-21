from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie, Review, Comment
from .serializers import MovieListSerializer, ReviewSerializer, CommentSerializer,MovieSerializer

import requests
api_key = '3a5a5d5bd9ebc60efe15703f924c7578'

@api_view(['GET'])
def getMovie(request):
    movies = Movie.objects.all()
    if not movies:
        url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=ko-kr'
        req = requests.get(url)
        for movie in req.json().get('results'):
            serializer = MovieListSerializer(data=movie)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        print(request.data)
        movie = get_object_or_404(Movie, pk=pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST','GET', 'DELETE', 'PUT'])
def review(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, movie=pk, pk=review_pk)
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
        serializer = ReviewSerializer(instance=review, data=request.data)
        movie = get_object_or_404(Movie, pk=pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        

@api_view(['POST','GET'])
def comment(request, pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, movie=pk, pk=review_pk)
    comment = get_object_or_404(Comment, Review=review, pk= comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review = review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
