from django.urls import include, path
from django.contrib import admin

from .views import user_view
from . import views

app_name = 'futebol'
urlpatterns = [
    #path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.user_view, name='user_view'),
]