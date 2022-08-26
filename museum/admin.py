from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'created_at', 'slug', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'anonse')


class CategoryNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ExposureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(PhotoCarusel)
admin.site.register(CategoryNews, CategoryNewsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Projects)
admin.site.register(Excursions)
admin.site.register(Exposure, ExposureAdmin)
admin.site.register(PhotoNews)
admin.site.register(PhotoExposure)
admin.site.register(EntryExcursions)
