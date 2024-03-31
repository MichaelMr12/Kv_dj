from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from humster.forms import AddPostForm
from humster.models import Women

menu = [{'title': 'главная', 'url_name': 'home'},
        {'title': 'добавить пост', 'url_name': 'addpost'},
        {'title': 'сп женщин id', 'url_name': 'womensid'},
        {'title': 'сп женщин слагам', 'url_name': 'womens-slug'},
        ]


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form,
    }

    return render(request, 'humster/addpost.html', context=data)


def show_womenid(request, id):
    id = get_object_or_404(Women, pk=id)

    data = {
        'title': id.title,
        'menu': menu,
        'id': id,

    }

    return render(request, 'humster/womenid.html', context=data)


def show_womensl(request, sl):
    id = get_object_or_404(Women, slug=sl)
    data = {

        'menu': menu,
        'id': id,

    }
    return render(request, 'humster/womenid.html', context=data)


def womensid(request):
    posts = Women.objects.all()
    data = {
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'humster/womensid.html', context=data)


def womensslug(request):
    posts = Women.objects.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'humster/womens-slug.html', context=data)


# Create your views here.
def index(request):
    return render(request, 'humster/index.html', {'menu': menu})


def animals(request):
    return render(request, 'humster/animals.html')


def kub(request):
    return render(request, 'humster/3D_kub.html')


def category(request, cat_id):
    data = {'cat_id': cat_id}
    return render(request, 'humster/cat_id.html', data)
    # ,return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p> Хомячок номер -<b>{cat_id}</b> </p>' )


def category_slug(request, cat_slug):
    data = {'cat_slug': cat_slug}
    return render(request, 'humster/cat_slug.html', data)
    # return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p>  категория -<b>{cat_slug}</b> </p>' )
