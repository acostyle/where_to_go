from django.contrib import admin
from .models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, 
    ]