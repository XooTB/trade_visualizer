from django.urls import path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

