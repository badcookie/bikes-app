from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json


def index(request):
    """Greets the World.

    Parameters
    ----------
    request
        HTTP request for '' url.

    Returns
    -------
        Response with a greeting string.

    """

    return HttpResponse("Hello, world. You're at the index.")


class CategoriesListView(ListView):
    """Handles requests on 'categories/' url."""

    def get(self, request, *args, **kwargs):
        """Handles GET request responding with categories list.

        Parameters
        ----------
        request
            HTTP GET request for 'categories/' url.
        args
            Signature argument.
        kwargs
            Signature argument.

        Returns
        -------
            Response with each category instance.

        """

        categories_list = list(Category.objects.all().values())
        categories_data = json.dumps(categories_list)
        return HttpResponse(categories_data)


class CategoryView(DetailView):
    """Handles requests on 'categories/<int:pk>/' url."""

    def get(self, request, *args, **kwargs):
        """Handles GET request responding with vehicles list.

        Parameters
        ----------
        request
            HTTP GET request for 'categories/<int:pk>/' url.
        args
            Signature argument.
        kwargs
            Storage for 'pk' query parameter.

        Returns
        -------
            Response with specific category vehicles.

        """

        category_id = kwargs['pk']
        category_name = get_object_or_404(Category, id=category_id).name
        vehicles_list = list(Motobike.objects.filter(category=category_name).values())
        category_data = json.dumps(vehicles_list)
        return HttpResponse(category_data)


class MotobikeView(DetailView):
    """Handles requests on 'details/<int:pk>/' url."""

    def get(self, request, *args, **kwargs):
        """Handles GET request responding with vehicle data.

        Parameters
        ----------
        request
            HTTP GET request for 'details/<int:pk>/' url.
        args
            Signature argument.
        kwargs
            Storage for 'pk' query parameter.

        Returns
        -------
            Response with specific vehicle data.

        """

        motobike_id = kwargs['pk']
        motobike_object = get_object_or_404(Motobike, id=motobike_id)
        motobike_data = json.dumps(model_to_dict(motobike_object))
        return HttpResponse(motobike_data)
