from django.urls import path

from . import views

app_name = 'hello'

urlpatterns = [
    path('owner', views.owner, name='owner'),
    path('', views.myview)
]

