from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
from django.shortcuts import get_object_or_404


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
        categories_list = [{"id": item.id, "name": item.name} for item in categories]

        return JsonResponse(categories_list, safe=False)


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
        motobikes = Motobike.objects.filter(category=category)
        category_vehicles_list = [
            {
                "id": item.id,
                "name": item.name,
                "vendor": item.company.name,
                "category": item.category.name,
                "description": item.description,
            }
            for item in motobikes
        ]

        return JsonResponse(category_vehicles_list, safe=False)


class MotobikeView(DetailView):
    """Handles requests on 'details/<int:pk>/' url."""

    model = Motobike

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

        vehicle = get_object_or_404(self.model, id=kwargs['pk'])
        vehicle_data = {
            "id": vehicle.id,
            "name": vehicle.name,
            "vendor": vehicle.company.name,
            "category": vehicle.category.name,
            "description": vehicle.description,
        }

        return JsonResponse(vehicle_data)
