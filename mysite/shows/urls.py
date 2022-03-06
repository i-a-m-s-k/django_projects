from django.urls import path
from . import views


# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'shows'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.ShowCreate.as_view(), name='show_create'),
    path('main/<int:pk>/update/', views.ShowUpdate.as_view(), name='show_update'),
    path('main/<int:pk>/delete/', views.ShowDelete.as_view(), name='show_delete'),
    path('lookup/', views.GenreView.as_view(), name='genre_list'),
    path('lookup/create/', views.GenreCreate.as_view(), name='genre_create'),
    path('lookup/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre_update'),
    path('lookup/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
]


