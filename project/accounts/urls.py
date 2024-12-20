from django.urls import path
from .views import *
from rest_framework.authtoken import views 

urlpatterns = [
    path('api-token/',views.obtain_auth_token)
]
