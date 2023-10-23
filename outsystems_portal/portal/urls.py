from django.urls import path
from .views import main, outsystems

urlpatterns = [
    path('home', main),
    path('outsystems', outsystems)
]