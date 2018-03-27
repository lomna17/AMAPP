# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:52:06 2018

@author: lomna
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'search.html', views.search, name="search")
]
