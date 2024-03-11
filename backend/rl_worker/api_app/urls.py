from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('v1/event/', views.get_event_list, name='calendar'),
] 