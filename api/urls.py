from django.urls import path
import api.views as views

app_name = 'api'

urlpatterns = [
    path('data/contacts/', views.contacts, name='contacts'),
    path('data/items/', views.items, name='items'),
    # path('data/data_from_index_page/', views.data_from_index_page, name='data_from_index_page'),

    path('account/status/', views.status, name='status'),
    path('account/login/', views.login_, name='login'),
    # path('account/reg/', views.reg, name='reg'),
    path('account/logout/', views.logout_, name='logout'),
]


