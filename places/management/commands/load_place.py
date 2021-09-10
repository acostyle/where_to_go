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

        place, created = Place.objects.update_or_create(
            title=new_place['title'],
            short_description=new_place['description_short'],
            long_description=new_place['description_long'],
            latitude=new_place['coordinates']['lat'],
            longitude=new_place['coordinates']['lng'],
            
        )

        image_files = os.listdir(settings.MEDIA_ROOT)
        for image in image_files:
            if image.startswith(place.title.replace(' ', '_')):
                os.remove(f'media/{image}')

        old_images_in_db = PlaceImage.objects.filter(place=place)
        old_images_in_db.delete()

        for picture_number, image_url in enumerate(new_place['imgs']):
            response = requests.get(image_url)
            response.raise_for_status()
            image = PlaceImage.objects.create(place=place, position=picture_number)
            image.image.save(
                f'{place.title}_{picture_number}.jpg',
                ContentFile(response.content),
                save=True
            )
        if created:
            self.stdout.write(f'New place {place.title} has been loaded.')
        else:
            self.stdout.write(
                f'The place {place.title} already exists, all photos have been replaced.'
            )