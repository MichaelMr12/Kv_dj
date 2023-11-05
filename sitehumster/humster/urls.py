

from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('cub/', views.kub),
    path('animals/', views.animals),
    path('cats/<int:cat_id>/', views.category),
    path('cats/<slug:cat_slug>/', views.category_slug),
]
