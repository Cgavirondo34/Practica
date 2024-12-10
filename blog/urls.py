from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_post/', views.add_post, name='add_post'),
    path('search_post/', views.search_post, name='search_post'),
]
