from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from moviebackend.auth import *
# from newsbackend.permissions import *
from django.contrib.auth.models import User
from .models import *
import random
import datetime
import re
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
# from django.conf import settings
from moviebackend import settings
from .serializers import *
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.


SECRET = getattr(settings,'SECRET','secret')

ALGO = getattr(settings,'ALGO','HS256')

#functions here

def sendmail(email,otp):
    subject = 'Your OTP to sign up on Sajjan Movies is '+otp
    context ={
        'otp':otp,
    }
    html_message = render_to_string('memail.html', context)
    recipient_list = [email]
    try:
     send_mail( subject,'Message not supported in HTML, enable HTML support' ,settings.Email_HOST_USER,recipient_list,
               fail_silently=False,html_message=html_message,auth_password=settings.Email_HOST_PASSWORD,auth_user=settings.Email_HOST_USER )
     return True
    except Exception as e:
     print(e)
     return False

#apis here

@api_view(['POST'])
def signupsendotp(request):
    try:
        email = request.data.get('email')
        if rUser.objects.filter(user_email=email).exists():
            return Response({'message':'Email already exists'},status=403)
        otp=str(random.randint(100000,999999))
        payload = {
                "otp": otp,
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
                "iat": datetime.datetime.utcnow(),
            }
        print(email,otp,sendmail(email,otp))
        # jwt.Encode(payload, SECRET, algorithm=ALGO)
        token = jwt.encode(payload, SECRET, algorithm=ALGO)
        # Send email
        print(token)
        return Response({'token':token,'message':'OTP Sent!'},status=200)
    except Exception as e:
        return Response({'message':str(e)},status=400)
    
@api_view(['POST'])
def signupverifyotp(request):
    try:
        otp = request.data.get('otp')
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = jwt.decode(token, SECRET, algorithms=ALGO)
        email=payload['email']
        if otp == payload['otp']:
            payload ={
                'email':email,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=129600),
                'iat':datetime.datetime.utcnow(),
            }
            token = jwt.encode(payload, SECRET, algorithm=ALGO)
            return Response({'token':token,'message':'OTP Verified!'},status=200)
        else:
            return Response({'message':'OTP Mismatch!'},status=403)
    except Exception as e:
        return Response({'message':str(e)},status=400)
    
@api_view(['POST'])
def adduser(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        payload = jwt.decode(token, SECRET, algorithms=ALGO)
        email=payload['email']
        if rUser.objects.filter(user_email=email).exists():
            return Response({'message':'Email already exists'},status=403)
        user_name = request.data.get('name')
        user_password = request.data.get('password')
        user_phone = request.data.get('phone')
        user_country = request.data.get('country')
        rUser.objects.create(user_name=user_name,user_email=email,user_password=user_password,user_phone=user_phone,user_country=user_country)
        return Response({'message':'User Added!'},status=200)
    except Exception as e:
        return Response({'message':str(e)},status=400)

@api_view(['POST'])
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        if rUser.objects.filter(user_email=email,user_password=password).exists():
            payload ={
                'email':email,
                'id':rUser.objects.get(user_email=email).user_id,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=129600),
                'iat':datetime.datetime.utcnow(),
            }
            token = jwt.encode(payload, SECRET, algorithm=ALGO)
            user=rUser.objects.get(user_email=email)
            serializer = UserSerializer(user)
            print(serializer.data)
            return Response({'token':token,'message':'Login Successful!','userd':serializer.data},status=200)
        else:
            return Response({'message':'Invalid Credentials!'},status=403)
    except Exception as e:
        return Response({'message':str(e)},status=400)