from django.db.models import fields
from rest_framework import serializers
from .models import Genre, Movie, Comment, Review,Game


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
    like_user = serializers.SerializerMethodField('user_like',read_only=True)

    def user_like(self, review):
        user = self.context.get('user')
        if review.like_users.filter(pk=user.pk).exists():
           return 1
        else:
            return 0
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    like_user = serializers.SerializerMethodField('user_like',read_only=True)

    def user_like(self, review):
        user = self.context.get('user')
        print(self.context)
        if review.like_users.filter(pk=user.pk).exists():
           return 1
        else:
            return 0 

    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Game
        fields = '__all__'