from django.contrib import admin

from shows.models import Genre, Show

# Register your models here.

admin.site.register(Genre)
admin.site.register(Show)