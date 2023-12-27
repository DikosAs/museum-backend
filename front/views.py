from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import *

# Create your views here.
def ru_index(request: WSGIRequest):
    context = {
        'contacts': Contacts.objects.all(),
        'content': DataFromIndexPage.objects.all()[0]
    }
    return render(request, "ru/index.html", context=context)


def ru_items(request: WSGIRequest):
    context = {
        "objacts": Objacts.objects.all(),
        "contacts": Contacts.objects.all()
        }
    return render(request, "ru/items-menu.html", context=context)


def en_index(request: WSGIRequest):
    context = {
        'contacts': Contacts.objects.all(),
        'content': DataFromIndexPage.objects.all()[0]
    }
    return render(request, "en/index.html", context=context)


def en_items(request: WSGIRequest):
    context = {
        "objacts": Objacts.objects.all(),
        "contacts": Contacts.objects.all()
        }
    return render(request, "en/items-menu.html", context=context)


def ud_index(request: WSGIRequest):
    context = {
        'contacts': Contacts.objects.all(),
        'content': DataFromIndexPage.objects.all()[0]
    }
    return render(request, "ud/index.html", context=context)


def ud_items(request: WSGIRequest):
    context = {
        "objacts": Objacts.objects.all(),
        "contacts": Contacts.objects.all()
        }
    return render(request, "ud/items-menu.html", context=context)
