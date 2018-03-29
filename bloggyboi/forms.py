# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:32:12 2018

@author: lomna
"""
from django import forms 
from .models import Post

variables = (("Auth", "author"),("Title", "title"),("Text", "text"),("Created", "created_date"),
                 ("Published", "published_date"),("Num","number"))

class DropDown(forms.Form):
    field = forms.ChoiceField(choices = variables)