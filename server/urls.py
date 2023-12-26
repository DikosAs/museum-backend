from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


def index_re(request):
    return redirect(reverse('ru:index'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('en/', include('en.urls')),
    path('ru/', include('ru.urls')),
    path('ud/', include('ud.urls')),
    path('', index_re),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)