from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'tt', views.get_global_trends, name='trends'),
    path(r'user/<str:user_name>', views.user, name='users'),
    path(r'search', views.search, name='search'),
    path(r'hash/<str:hash_name>', views.hash, name='hash'),
    path(r'country/<str:name>/<int:id>', views.country, name='country'),
]
