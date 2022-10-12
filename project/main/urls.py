from unittest.mock import patch
from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetableView, name = 'timetable-main')
]
