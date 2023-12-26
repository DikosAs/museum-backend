from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'ru'


def index_re(request):
    return redirect(reverse('index'))


urlpatterns = [
    path('index.html', index, name='index'),
    path('items.html', items, name='items'),
    path('', index_re)
]