from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'humster/index.html')


def category(request, cat_id):
    data = {'cat_id': cat_id}
    return render(request, 'humster/cat_id.html', data)
    # ,return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p> Хомячок номер -<b>{cat_id}</b> </p>' )


def category_slug(request, cat_slug):
    data = {'cat_slug': cat_slug}
    return render(request, 'humster/cat_slug.html', data)
    # return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p>  категория -<b>{cat_slug}</b> </p>' )
