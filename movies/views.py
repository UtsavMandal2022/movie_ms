from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.pagination import PageNumberPagination
import json
from rest_framework.parsers import MultiPartParser, FormParser
from moviebackend.auth import *

#landing page

def landing_page(request):
    return render(request,'./index.html')

# Create your views here.

@api_view(['GET'])
@authentication_classes([UserAuthentication])
def get_movies(request):
    try:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['GET'])
@authentication_classes([UserAuthentication])
def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['POST'])
@authentication_classes([UserAuthentication])
def add_movie(request):
    try:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie added successfully'})
        else:
            return Response({'error': serializer.errors})
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['PUT'])
@authentication_classes([UserAuthentication])
def update_movie(request, movie_id):
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie updated successfully'})
        else:
            return Response({'error': serializer.errors})
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['DELETE'])
@authentication_classes([UserAuthentication])
def delete_movie(request, movie_id):
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'})
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['GET'])
@authentication_classes([UserAuthentication])
def get_movie_by_genre(request, movie_genre):
    try:
        movies = Movie.objects.filter(movie_genre=movie_genre)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)})
    
@api_view(['GET'])
@authentication_classes([UserAuthentication])
def get_movie_by_language(request, movie_language):
    try:
        movies = Movie.objects.filter(movie_language=movie_language)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)})
    
# @api_view(['POST'])
# @authentication_classes([UserAuthentication])
# def send_email(request):
#     try:
#         data = request.data
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         print(email, subject, message)
#         print(settings.Email_HOST_USER,settings.Email_HOST_PASSWORD)
#         send_mail(subject, message, settings.Email_HOST_USER, [email], fail_silently=False)
#         return Response({'message': 'Email sent successfully'}, status=200)
#     except:
#         return Response({'message': 'Error sending email'}, status=400)