from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('addpost/', addpost, name='addpost'),
    path('cub/', kub),
    path('animals/', animals),
    path('cats/<int:cat_id>/', category),
    path('cats/<slug:cat_slug>/', category_slug),
    path('womenid/<int:id>/', show_womenid, name='womenid'),
    path('womensid/', womensid, name='womensid'),
    path('womenslug/<slug:sl>/', show_womensl, name='womenslug'),
    path('womens-slug/', womensslug, name='womens-slug'),
    path('about/', about, name='about'),
]
