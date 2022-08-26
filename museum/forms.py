from django import forms
from .models import Excursions
from django.core.validators import RegexValidator


class EntryExcursionsForm(forms.Form):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Введите своё имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": 'form-control', 'placeholder': 'Введите свой email'}))
    excursion = forms.ModelChoiceField(empty_label='Выберите экскурсию', label='Экскурсия', queryset=Excursions.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Тема', widget=forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'Введите сообщение: количество человек, предпочтительную дату экскурсии, дополнительные детали'}))
    phonenumber = forms.CharField(label='Номер телефона', validators=[phoneNumberRegex], max_length=16, widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Введите свой номер телефона в формате +7xxxxxxxxxx'}))



class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Введите тему обращения'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": 'form-control', 'placeholder': 'Введите свой email'}))
    content = forms.CharField(label='Тема', widget=forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'Введите сообщение'}))


