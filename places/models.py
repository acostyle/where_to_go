from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Место."""
    title = models.CharField("Название места", max_length=200, db_index=True)
    short_description = models.TextField(
        "Краткое описание",
        blank=True
    )
    long_description = HTMLField("Полное описание", blank=True)
    latitude = models.DecimalField(
        "Широта",
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        "Долгота",
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.title}"


class PlaceImage(models.Model):
    """Изображение места."""
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="place_images",
        verbose_name="Место",
        )
    image = models.ImageField("Изображение места", upload_to="")
    position = models.PositiveIntegerField("Позиция", db_index=True, null=True, blank=True)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f"{self.id} - {str(self.place)}"
