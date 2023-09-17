from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('страница приложения humster' )

def category(request, cat_id):
    return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p> Хомячок номер -<b>{cat_id}</b> </p>' )