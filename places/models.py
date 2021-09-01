from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Место."""
    title = models.CharField("Название места", max_length=200, db_index=True)
    description_short = models.TextField(
        "Краткое описание",
        null=True,
        blank=True
    )
    description_long = HTMLField("Полное описание", null=True, blank=True)
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
    image = models.ImageField("Изображение места", upload_to="place_images")
    position = models.PositiveIntegerField("Позиция", null=True, unique=True)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f"{self.id} - {str(self.place)}"
