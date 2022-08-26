from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from .forms import EntryExcursionsForm, ContactForm
from django.core.mail import send_mail
from django.contrib import messages


class NewsView(ListView):
    model = News
    template_name = 'museum/Новости.html'
    context_object_name = 'news'
    categories = CategoryNews.objects.all()
    extra_context = {'categories': categories}
    paginate_by = 10


class ExposureView(ListView):
    model = Exposure
    template_name = 'museum/Экспозиции.html'
    context_object_name = 'exposure'


def index(request):
    newss = News.objects.all()[:3]
    categories = News.objects.all()
    projects = Projects.objects.all()
    carousel = PhotoCarusel.objects.all()
    context = {
        'news': newss,
        'categories': categories,
        'projects': projects,
        'carousel': carousel,
    }
    return render(request, template_name='museum/Главная.html', context=context)


def get_category(request, slug):
    categories = CategoryNews.objects.all()
    category = CategoryNews.objects.get(slug=slug)
    newss = News.objects.filter(category=category)
    paginator = Paginator(newss, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'museum/Новости.html',
                  {'news': newss, 'categories': categories, 'category': category, 'page_obj': page_obj})


def exposure(request):
    exposures = Exposure.objects.all()
    context = {
        'exposure': exposures,
    }
    return render(request, template_name='museum/Экспозиции.html', context=context)


def news_single(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {
        'news': news,
    }
    return render(request, 'museum/Новости-сингл.html', context=context)


def exposure_single(request, slug):
    exposures = get_object_or_404(Exposure, slug=slug)
    context = {
        'exposure': exposures,
    }
    return render(request, 'museum/Экспозиции-сингл.html', context=context)


def entry_excursion(request):
    if request.method == 'POST':
        form = EntryExcursionsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phonenumber']
            excursion = form.cleaned_data['excursion']
            message = 'Письмо было отправлено с сайта, адрес для ответа %s \r\n \r\n' % sender
            message += form.cleaned_data['message']
            message += '\r\nИмя: %s \r\n' % name
            message += 'Телефон: %s \r\n' % phoneNumber
            message += 'Экскурсия: %s' % excursion
            recipients = ['visitvmusei@yandex.ru']
            # и отправим его
            mail = send_mail(excursion, message, 'ghjuhfghb@yandex.ru', recipients, fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка отправки, проверьте данные!')
    else:
        form = EntryExcursionsForm()
    return render(request, 'museum/ЗаписьЭкскурсии.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            email = form1.cleaned_data['email']
            recipients = ['visitvmusei@yandex.ru']
            message = 'Письмо от %s \r\n' % email
            message += form1.cleaned_data['content']
            mail = send_mail(form1.cleaned_data['subject'], message, 'ghjuhfghb@yandex.ru', recipients, fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка отправки, проверьте данные!')
    else:
        form1 = ContactForm()
    return render(request, 'museum/ОбратнаяСвязь.html', {'form': form1})

