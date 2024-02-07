from django.contrib import admin
from api.models import Contacts, DataFromIndexPage, Items


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'img')


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('ru_title', 'ru_description', 'ud_title', 'ud_description', 'en_title', 'en_description', 'img')


class DataFromIndexPageAdmin(admin.ModelAdmin):
    list_display = ('type', 'ru_text', 'ud_text', 'en_text')


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(DataFromIndexPage, DataFromIndexPageAdmin)

