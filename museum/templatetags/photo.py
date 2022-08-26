from django import template
from museum.models import *

register = template.Library()


@register.inclusion_tag('museum/Главная.html')
def get_photo():
    photos = PhotoNews.objects.all()
