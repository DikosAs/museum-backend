from django.contrib import admin
from .models import *


# Register your models here.
class ObjactsAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "show_image"]


class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url", "image", "show_image"]


# соединяем класс и модель
admin.site.register(Objacts, ObjactsAdmin)
admin.site.register(Contacts, ContactsAdmin)
