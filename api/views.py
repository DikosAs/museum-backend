from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from api.models import Contacts, Items


# Create your views here.
def items(request: WSGIRequest):
    if not (request.method == 'GET'):
        return JsonResponse({"status": "400 Bad request"}, status=400)

    items_ = []
    for item in Items.objects.all():
        if item.img:
            img = item.img.url
        else:
            img = ""
        items_.append({
            "title_map": {
                "ru": {
                    "description": item.ru_description,
                    "title": item.ru_title
                },
                "en": {
                    "description": item.en_description,
                    "title": item.en_title
                },
                "ud": {
                    "description": item.ud_description,
                    "title": item.ud_title
                }
            },
            "img": img
        })

    return JsonResponse({"status": "200 OK", "items": items_})


def contacts(request: WSGIRequest):
    if not (request.method == 'GET'):
        return JsonResponse({"status": "400 Bad request"}, status=400)

    contacts_ = []
    for contact in Contacts.objects.all():
        contacts_.append({
            "url": contact.url,
            "img": contact.img.url,
            "title": contact.title
        })

    return JsonResponse({"status": "200 OK", "contacts": contacts_})


def status(request: WSGIRequest):
    if not (request.method == 'GET'):
        return JsonResponse({"status": "400 Bad request"}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"status": "200 OK", "username": ""})

    return JsonResponse({"status": "200 OK", "username": request.user.username})


def login_(request: WSGIRequest, username: str, password: str):
    if request.method == 'GET':
        return JsonResponse({"status": "400 Bad request"})

    if request.user.is_authenticated:
        return JsonResponse({"status": "200 OK"})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": "200 OK", "username": username})
    else:
        return JsonResponse({"status": "401 Unauthorized", "message": "Wrong username or password"})


def logout_(request: WSGIRequest):
    if request.method == 'GET':
        return JsonResponse({"status": "400 Bad request"})

    if not request.user.is_authenticated:
        return JsonResponse({"status": "401 Unauthorized"})

    logout(request)
    return JsonResponse({"status": "200 OK"})
