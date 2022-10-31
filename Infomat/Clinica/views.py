from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView

from Clinica.admin import AllPostAdmin
from Clinica.models import AllPost


# Create your views here.
# You can work with Django Class.Watch dockumentation
def index(request):
    return render(request, 'Clinica/index.html')


# def news(request):
#    return render(request, 'Clinica/news.html')


class News(ListView):  # in listview есть пагинатор для отображения страниц
    paginate_by = 4  # количество постов на одной странице
    model = AllPost  # обязательно наличие модели для данного представления!
    template_name = 'Clinica/news.html'
    context_object_name = 'posts'  # переменная используемая в шаблоне при работе с бд
    print()

    def get_queryset(self):
        return AllPost.objects.filter(
            is_published=True)  # возвращает только опубликованные в админке записи(выбранные из модели) на страницу


def show_news(request, post):
    print("Request ->", request)
    if request.GET:
        print("Request.GET ->", request.GET)
    return HttpResponse(f"<h1>Pages to news on 1 news</h1><p>{post}</p>")


def arhiv_news(request):
    return render(request, 'Clinica/arhiv_news.html')


def archive(request, year):
    if int(year) > 2022:
        return redirect('index')
    return HttpResponse(f"<h2>Страница для архива по годам</h2><p>{year}</p>")


def contact(request):
    return render(request, 'Clinica/contact.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")
