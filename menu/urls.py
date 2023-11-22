from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import *
app_name = "menu"


urlpatterns = [
    path('', views.menu_record, name='menu'),

]