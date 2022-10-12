from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),      #слайд шоу,6важных новостей с переходом ко всем новостям
    path('news/', news, name='news'),       #здесь новости организованы по 5 шт по вертикали с погинацией
    path('news/<slug:post>/', show_news, name='show_news'),     #заготовка под генерацию собственных страниц
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  #после слова archive идет формирование свое страницы
    path('contact/', contact, name='contact'),      #информация о юридическом адресе организации и контактах основных служб

]
