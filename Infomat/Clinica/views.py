from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# You can work with Django Class.Watch dockumentation
def index(request):
    return render(request, 'Clinica/index.html')

def news(request):
    return render(request, 'Clinica/news.html')

def show_news(request,news):
    if request.GET:
        print(request.GET)
        print(request)
    return HttpResponse(f"<h1>Pages to news on 1 news</h1><p>{news}</p>")
def contact(request):
    return render(request, 'Clinica/contact.html')
