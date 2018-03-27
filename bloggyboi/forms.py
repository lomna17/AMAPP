# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:32:12 2018

@author: lomna
"""
from django import forms 
from .models import Post

variables = ("author","title","text","created_date","published_date","number")

class DropDown(forms.Form):
    class Meta:
        model = Post
        fields = ["field"]