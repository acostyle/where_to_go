from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def show_index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(
                        'show_place_details', args=[place.id]
                    ),
                }
            }
        )

    context = {
        'places': places_geojson
    }

    return render(request, 'index.html', context)


def show_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    places_images = place.place_images.all()

    place_parameters = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in places_images],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {"lng": place.longitude, "lat": place.latitude}
    }

    return JsonResponse(
        place_parameters,
        safe=False,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4
        }
    )
