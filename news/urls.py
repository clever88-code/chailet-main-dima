from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import *
app_name = "news"


urlpatterns = [
    path('', views.news_record, name='news'),

]