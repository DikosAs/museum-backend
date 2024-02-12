from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
