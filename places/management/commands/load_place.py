from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import PlaceImage, Place
from django.conf import settings
import requests
import os


class Command(BaseCommand):
    help = 'Load a Place from JSON'

    def add_arguments(self, parser):
        parser.add_argument('json', help='Place JSON URL')


    def handle(self, *args, **options):
        response = requests.get(options['json'])
        response.raise_for_status()
        new_place = response.json()

        place_to_save = {}
        place_to_save['short_description'] = new_place['description_short']
        place_to_save['long_description'] = new_place['description_long']
        place_to_save['latitude'] = new_place['coordinates']['lat']
        place_to_save['longitude'] = new_place['coordinates']['lng']

        place, place_created = Place.objects.update_or_create(
            title=new_place['title'],
            defaults = place_to_save
        )

        if place_created:
            for picture_number, image_url in enumerate(new_place['imgs']):
                response = requests.get(image_url)
                response.raise_for_status()
                image, image_created = PlaceImage.objects.update_or_create(
                    place=place,
                    position=picture_number
                )
                image.image.save(
                    f'{place.title}_{picture_number}.jpg',
                    ContentFile(response.content),
                    save=True
                )


            

        if place_created and image_created:
            self.stdout.write(f'New place {place.title} has been loaded.')
        if not place_created: 
            self.stdout.write(
                f'The place {place.title} already exists, all photos have been replaced.'
            )           