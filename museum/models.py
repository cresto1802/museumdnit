from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from sorl.thumbnail import ImageField, get_thumbnail


class PhotoCarusel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото карусели')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Фото для карусели'
        verbose_name_plural = 'Фото для карусели'


class CategoryNews(models.Model):
    title = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название новости')
    anonse = models.CharField(max_length=250, verbose_name='Анонс новости', )
    content = models.TextField(blank=True, verbose_name='Контент новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')
    category = models.ForeignKey(CategoryNews, on_delete=models.PROTECT, related_name='news_cat', verbose_name='Категория')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Главное фото новости')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_single', kwargs={"slug": self.slug})


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class PhotoNews(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='photonews')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото новости')
    index = models.IntegerField(verbose_name='Индекс')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-news']
        verbose_name = 'Фото для новостей'
        verbose_name_plural = 'Фото для новостей'


class Excursions(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание экскурсии')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'


class Projects(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название проекта')
    content = models.TextField(blank=True, verbose_name='Описание проекта')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото проекта')
    link = models.URLField(verbose_name='Ссылка на проект', default='home.ru', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Exposure(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название экспозиции')
    adress = models.CharField(max_length=250, verbose_name='Адрес')
    arter_name = models.CharField(max_length=250, verbose_name='Художник-монументалист')
    transport = models.CharField(max_length=250, verbose_name="Остановки транспорта", default='Дом науки и техники')
    content = models.TextField(blank=True, verbose_name='Описание(основной текст)')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Главное фото экспозиции')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exposure_single', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Экспозиция'
        verbose_name_plural = 'Экспозиции'


class PhotoExposure(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    exposure = models.ForeignKey(Exposure, on_delete=models.PROTECT, related_name='exposurephoto')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото экспозиции')
    index = models.IntegerField(verbose_name='Индекс')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-exposure']
        verbose_name = 'Фото для Экспозиций'
        verbose_name_plural = 'Фото для Экспозиций'


class EntryExcursions(models.Model):
    name = models.CharField(max_length=250, verbose_name='Фио')
    email = models.EmailField(max_length=255, verbose_name='Емэйл')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name='Номер телефона')
    excursion = models.ForeignKey(Excursions, on_delete=models.PROTECT, verbose_name='Экскурсия', related_name='excursions')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-excursion']
        verbose_name = 'Запись на экскурсию'
        verbose_name_plural = 'Записи на экскурсии'
