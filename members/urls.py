# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:36:10 2023

@author: user
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
