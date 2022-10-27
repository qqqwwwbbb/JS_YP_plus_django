from django.urls import path

from .views import *

urlpatterns = [
    path('', test, name='test'),
    path('genre/<int:pk>', get_genre, name='genre'),
]