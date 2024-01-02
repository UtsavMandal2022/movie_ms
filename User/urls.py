from django.urls import path
from .views import *

urlpatterns = [
    path('signupsendotp/',signupsendotp),
    path('signupverifyotp/',signupverifyotp),
    path('adduser/',adduser),
    path('login/',login),
]