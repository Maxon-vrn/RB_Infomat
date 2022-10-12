from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),      #слайд шоу,6важных новостей с переходом ко всем новостям
    path('news/', news, name='news'),       #здесь новости организованы по 5 шт по вертикали с погинацией
    path('news/<slug:news>/', show_news, name='show_news'),     #заготовка под генерацию собственных страниц
    path('contact/', contact, name='contact'),      #информация о юридическом адресе организации и контактах основных служб

]
