from django.db.models import fields
from rest_framework import serializers
from .models import Genre, Movie, Comment, Review


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('Review',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.email')
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    movie = serializers.ReadOnlyField(source='movie.title')
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'