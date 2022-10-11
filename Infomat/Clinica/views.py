from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# You can work with Django Class.Watch dockumentation
def index(request):
    return render(request, 'Clinica/index.html')


def contact(request):
    return render(request, 'Clinica/contact.html')
