from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request: WSGIRequest):
    context = {"contacts": Contacts.objects.all()}
    return render(request, "en/index.html", context=context)


def items(request: WSGIRequest):
    context = {
        "objacts": Objacts.objects.all(),
        "contacts": Contacts.objects.all()
        }
    return render(request, "en/items-menu.html", context=context)
