from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class CategoriesListView(ListView):
    def get(self, request, *args, **kwargs):
        categories_list = list(Category.objects.all().values())
        categories_data = json.dumps(categories_list)
        return HttpResponse(categories_data)


class CategoryView(DetailView):
    def get(self, request, *args, **kwargs):
        category_id = kwargs['pk']
        category_name = get_object_or_404(Category, id=category_id).name
        vehicles_list = list(Motobike.objects.filter(category=category_name).values())
        category_data = json.dumps(vehicles_list)
        return HttpResponse(category_data)


class MotobikeView(DetailView):
    def get(self, request, *args, **kwargs):
        motobike_id = kwargs['pk']
        motobike_object = get_object_or_404(Motobike, id=motobike_id)
        motobike_data = json.dumps(model_to_dict(motobike_object))
        return HttpResponse(motobike_data)
