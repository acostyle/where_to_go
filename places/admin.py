from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["get_preview"]
    fields = ("image", "get_preview")

    def get_preview(self, instance):
        return format_html(
            f'<img style="max-width: 200px;" src="{instance.image.url}"/>'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
