from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoriesListView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view()),
    path('details/<int:pk>/', views.MotobikeView.as_view()),
]
