from django.db import models

class Place(models.Model):
    title = models.CharField("Название места", max_length=200, db_index=True)
    description_short = models.TextField("Краткое описание", null=True, blank=True)
    description_long = models.TextField("Полное описание", null=True, blank=True)
    latitude = models.FloatField("Широта", null=True, blank=True)
    longitude = models.FloatField("Долгота", null=True, blank=True)

    def __str__(self):
        return self.title