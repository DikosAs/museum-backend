from django.urls import path, include, reverse
from django.shortcuts import redirect
from .views import *


def index_re(request):
    return redirect(reverse('ru_index'))


def re_ru_index(request):
    return redirect(reverse('ru_index'))


def re_en_index(request):
    return redirect(reverse('en_index'))


def re_ud_index(request):
    return redirect(reverse('ud_index'))


urlpatterns = [
    path('ru/', re_ru_index),
    path('en/', re_en_index),
    path('ud/', re_ud_index),
    path('ru/index.html', ru_index, name='ru_index'),
    path('ru/items.html', ru_items, name='ru_items'),
    path('en/index.html', en_index, name='en_index'),
    path('en/items.html', en_items, name='en_items'),
    path('ud/index.html', ud_index, name='ud_index'),
    path('ud/items.html', ud_items, name='ud_items'),
    path('', index_re),
]
