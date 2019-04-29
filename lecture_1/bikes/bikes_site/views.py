from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
import json
from django.shortcuts import get_object_or_404


# Создайте представления, исходя из urls
