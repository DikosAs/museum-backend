from django.db import models
from django.contrib import admin


# Create your models here.
class Objacts(models.Model):
    LANGS = (
        ('en', 'Английский'),
        ('ru', 'Русский'),
        ('ud', 'Удмуртский')
    )

    id = models.AutoField(primary_key=True)\

    ru_title = models.CharField(verbose_name="Название предмета (ру)", max_length=128)
    en_title = models.CharField(verbose_name="Название предмета (en)", max_length=128)
    ud_title = models.CharField(verbose_name="Название предмета (удм)", max_length=128)

    ru_description = models.TextField(verbose_name="Описание предмета (ру)", default=None, blank=True, null=True)
    en_description = models.TextField(verbose_name="Описание предмета (en)", default=None, blank=True, null=True)
    ud_description = models.TextField(verbose_name="Описание предмета (удм)", default=None, blank=True, null=True)

    image = models.ImageField(verbose_name="Изображение предмета", upload_to="objacts_img",
                              default=None, blank=True, null=True)

    @admin.display(description="Картинка")
    def show_image(self):
        from django.utils import html
        if self.image:
            return html.format_html("<img src='{}' style ='width:100px;'>", self.image.url)

    class Meta:
        verbose_name = "предмета"
        verbose_name_plural = "Предметы"


class Contacts(models.Model):
    title = models.CharField(verbose_name="Название сети", max_length=128)
    url = models.CharField(verbose_name="Ссылка на сеть", max_length=128)
    image = models.ImageField(verbose_name="Логотип сети", upload_to="contacts")

    @admin.display(description="Картинка")
    def show_image(self):
        from django.utils import html
        if self.image:
            return html.format_html("<img src='{}' style ='width:100px;'>", self.image.url)

    class Meta:
        verbose_name = "контакта"
        verbose_name_plural = "Контакты"


class DataFromIndexPage(models.Model):
    ru_text = models.TextField(verbose_name="Текст на русском")
    ud_text = models.TextField(verbose_name="Текст на удмуртском")
    en_text = models.TextField(verbose_name="Текст на английском")
