from django.db import models
from django.urls import reverse


# Create your models here.
class AllPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', default=' ',help_text="Заголовок")  # name model avto
    description = models.TextField(verbose_name='Описание статьи', default=' ', help_text="Описание статьи")  # max_length?
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', default=' ')  # 1 слайд
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', default=' ', blank=True)  # 2 слайд
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', default=' ', blank=True)  # 3 слайд
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', default=' ', blank=True)  # 4 слайд
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', default=' ', blank=True)  # 5 слайд
    text = models.TextField(verbose_name='Содержание статьи', default=' ', help_text="Содержание статьи",blank=True)  # max_length?
    responsible = models.CharField(max_length=255, verbose_name='Ответственный', default=' ', help_text="Ответственный")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):  # AllPost.objects.all() -> shell :<QuerySet [<Car: Camry>, <Car: Laurel>]>
        # эта конструкция возвращает заготловок текущей записи
        return self.title

    def get_absolute_url(self):  # кнопка смотреть на сайте
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta():  # замена имени в админ панели
        verbose_name = 'AllPosts'
        verbose_name_plural = 'Посты на странице'
        ordering = ['time_create']      # сортировка по значению/полю
