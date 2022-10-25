from multiprocessing.connection import Client
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class AllPostAdmin(admin.ModelAdmin):
    list_display =('id','title','text','responsible','get_html_photo','photo2','photo3','photo4','photo5','is_published')
    list_display_links = ('id', 'title')  # поля на которые мы можем кликнут  и перейти
    search_fields = ('title', 'text')  # по каким поля м можно искать информацию
    list_editable = ('is_published',)  # возможноть снимать с публикации рчерез админку
    list_filter = ('is_published', 'time_create')  # настройка фильтрации по полям

    def get_html_photo(self,object):    #отображение миниатюры фотографии авто в админ панели
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')
    get_html_photo.short_description = 'Миниатюра'

admin.site.register(AllPost, AllPostAdmin)