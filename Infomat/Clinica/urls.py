from django.urls import path, re_path
from .views import *
from django.views.generic import TemplateView   #ллассы представлений
from django.views.i18n import JavaScriptCatalog     #для подключение AdminDateTime

urlpatterns = [
    path('', index, name='index'),      #слайд шоу,6важных новостей с переходом ко всем новостям
    path('news/', News.as_view(), name='news'),       #здесь новости организованы по 5 шт по вертикали с погинацией
    path('arhiv_news/', arhiv_news, name='arhiv_news'),
    path('news/<slug:post>/', show_news, name='show_news'),     #заготовка под генерацию собственных страниц
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  #после слова archive идет формирование свое страницы
    path('contact/', contact, name='contact'),      #информация о юридическом адресе организации и контактах основных служб

]
