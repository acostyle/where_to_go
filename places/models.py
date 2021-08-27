from django.db import models
from django.db.models.base import Model


class Place(models.Model):
    """Место."""
    title = models.CharField("Название места", max_length=200, db_index=True)
    description_short = models.TextField("Краткое описание", null=True, blank=True)
    description_long = models.TextField("Полное описание", null=True, blank=True)
    latitude = models.FloatField("Широта", null=True, blank=True)
    longitude = models.FloatField("Долгота", null=True, blank=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    """Изображение места."""
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="place_images",
        verbose_name="Место",
        )
    url = models.ImageField("Изображение места", upload_to="place_images")
    
    def __str__(self):
        return f"{self.id} - {str(self.place)}"