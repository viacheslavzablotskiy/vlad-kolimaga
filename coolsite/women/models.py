from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикации')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')#, related_name='get_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные люди'
        verbose_name_plural = 'Известные люди'
        ordering = ['-time_create', 'title']#тобы группировка прошла успешно лучше эту строку поставить в комментарий
        #Выйти из самой оболочки , зайти обратно импротуировать все модули и начать работ (хотя она должна рработать и
        #сортировкой


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']