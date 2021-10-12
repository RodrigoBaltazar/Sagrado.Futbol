from django.urls import path

from . import views

app_name = 'futebol'
urlpatterns = [
    path('', views.index, name='index'),
]