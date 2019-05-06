from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
from django.shortcuts import get_object_or_404
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
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

    model = Category

    def get_queryset(self):
        """Defines a default query to be returned.

        Returns
        -------
            QuerySet of all categories' data.
        """

        return Category.objects.all().values()

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

        categories = self.get_queryset()
        return JsonResponse(list(categories), safe=False)


class CategoryView(ListView):
    """Handles requests on 'categories/<int:pk>/' url."""

    model = Category

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

        category = get_object_or_404(self.get_queryset(), id=kwargs['pk'])
        query = (
            Motobike.objects.filter(category_id=category.id)
            .annotate(vendor=F('company_id__name'))
            .values('name', 'vendor', 'description')
            .annotate(category=Value(category.name, output_field=CharField()))
        )

        return JsonResponse(list(query), safe=False)


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

        try:
            query = (
                Motobike.objects.annotate(vendor=F('company_id__name'))
                .values('name', 'vendor', 'description')
                .annotate(category=F('category_id__name'))
                .values('name', 'vendor', 'description', 'category')
                .get(id=motobike_id)
            )
        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        motobike_data = json.dumps(query)
        return HttpResponse(motobike_data)
