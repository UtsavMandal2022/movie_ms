from django.urls import path
from .views import *

urlpatterns = [
    path('getmovies/', get_movies),
    path('getmovie/<str:movie_id>', get_movie),
    path('addmovie/', add_movie),
    path('updatemovie/<str:movie_id>', update_movie),
    path('deletemovie/<str:movie_id>', delete_movie),
    path('getmoviesbygenre/<str:movie_genre>', get_movie_by_genre),
    path('getmoviesbylanguage/<str:movie_language>', get_movie_by_language),
]
