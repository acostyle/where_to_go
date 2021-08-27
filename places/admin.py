from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["placeimage_preview",]
    
    def placeimage_preview(self, obj):
        return format_html(
            f'<img src="{mark_safe(obj.url.url)}" height={200} width={400}/>'
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, 
    ]