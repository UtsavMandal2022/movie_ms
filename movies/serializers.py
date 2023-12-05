from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name', 'movie_genre', 'movie_year', 'movie_rating', 'movie_release_date', 'movie_language', 'movie_cast', 'movie_director', 'movie_runtime', 'movie_description']