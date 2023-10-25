from django.urls import path
from .import views

app_name = 'portal'
urlpatterns = [
    path('home', views.main),
    path('outsystems', views.outsystems),
    path('add-form', views.addform),
    path('saveRecord', views.saveRecord, name='saveRecord'),
    path('portalInit', views.portalInit, name='portalInit')
]