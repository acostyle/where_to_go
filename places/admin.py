from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["get_preview",]
    fields = ("url", "get_preview")

    def get_preview(self, obj):
        return format_html(
            f'<img style="max-width: 200px; height: auto;" src="{mark_safe(obj.url.url)}" height={obj.url.height} width={obj.url.width}/>'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, 
    ]