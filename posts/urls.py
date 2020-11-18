from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list_check/', views.list_check, name = 'list_check'),
    path('search/', views.search, name = 'search'),
    path('search_result/', views.search_result, name = 'search_result')
]