# Generated by Django 4.0.6 on 2022-07-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Excursions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Описание экскурсии')),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсии',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Exposure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название экспозиции')),
                ('adress', models.CharField(max_length=250, verbose_name='Адрес')),
                ('arter_name', models.CharField(max_length=250, verbose_name='Художник-монументалист')),
                ('transport', models.CharField(default='Дом науки и техники', max_length=250, verbose_name='Остановки транспорта')),
                ('content', models.TextField(blank=True, verbose_name='Описание(основной текст)')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')),
            ],
            options={
                'verbose_name': 'Экспозиция',
                'verbose_name_plural': 'Экспозиции',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название новости')),
                ('anonse', models.CharField(max_length=250, verbose_name='Анонс новости')),
                ('content', models.TextField(blank=True, verbose_name='Контент новости')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Url-слаг')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='news_cat', to='museum.categorynews', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCarusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото карусели')),
            ],
            options={
                'verbose_name': 'Фото для карусели',
                'verbose_name_plural': 'Фото для карусели',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название проекта')),
                ('content', models.TextField(blank=True, verbose_name='Описание проекта')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото проекта')),
                ('link', models.URLField(blank=True, default='home.ru', verbose_name='Ссылка на проект')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото новости')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='news_photo', to='museum.news')),
            ],
            options={
                'verbose_name': 'Фото для новостей',
                'verbose_name_plural': 'Фото для новостей',
                'ordering': ['-news'],
            },
        ),
        migrations.CreateModel(
            name='PhotoExposure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото экспозиции')),
                ('exposure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exposure_photo', to='museum.exposure')),
            ],
            options={
                'verbose_name': 'Фото для Экспозиций',
                'verbose_name_plural': 'Фото для Экспозиций',
                'ordering': ['-exposure'],
            },
        ),
    ]
