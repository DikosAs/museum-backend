from django.urls import path
import api.views as views

app_name = 'api'

urlpatterns = [
    path('data/contacts/', views.contacts, name='contacts'),
    path('data/items/', views.items, name='items'),
]
