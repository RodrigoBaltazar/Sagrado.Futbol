from django.urls import include, path
from django.contrib import admin

from . import views

app_name = 'futebol'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]