from django.contrib import admin
from .models import Anime, Gener, Direction, Reviews

@admin.register(Gener)
class GenerAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'date_pupl')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'anime')
