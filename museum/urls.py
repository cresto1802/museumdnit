from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('category_news/<str:slug>/', get_category, name='category'),
    path('news/', NewsView.as_view(), name='news'),
    path('exposure/', ExposureView.as_view(), name='exposure'),
    path('news/<str:slug>/', news_single, name='news_single'),
    path('exposures/<str:slug>/', exposure_single, name='exposure_single'),
    path('entry_excursion/', entry_excursion, name='entry_excursion'),
    path('contact_us/', contact_us, name='contact_us')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
