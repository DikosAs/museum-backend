from django.db import models


# Create your models here.
class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Название", max_length=255)
    url = models.CharField("Ссылка", max_length=255)
    img = models.ImageField("Изображение", blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class DataFromIndexPage(models.Model):
    TYPES = (

    )
    id = models.AutoField(primary_key=True)
    type = models.CharField("Место где отображать", max_length=5, choices=TYPES)
    ru_text = models.TextField("Текст на русском", blank=True, null=True)
    ud_text = models.TextField("Текст на удмуртском", blank=True, null=True)
    en_text = models.TextField("Текст на английском", blank=True, null=True)

    class Meta:
        verbose_name = 'Данные из главной страницы'
        verbose_name_plural = 'Данные из главной страницы'


class Items(models.Model):
    id = models.AutoField(primary_key=True)

    ru_description = models.TextField("Описание на русском", blank=True, null=True)
    ru_title = models.CharField("Название на русском", max_length=255, blank=True, null=True)

    ud_description = models.TextField("Описание на удмуртском", blank=True, null=True)
    ud_title = models.CharField("Название на удмуртском", max_length=255, blank=True, null=True)

    en_description = models.TextField("Описание на английском", blank=True, null=True)
    en_title = models.CharField("Название на английском", max_length=255, blank=True, null=True)

    img = models.ImageField("Изображение", blank=True, null=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
