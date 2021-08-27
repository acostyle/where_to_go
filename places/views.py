from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import JsonResponse

from places.models import Place, PlaceImage

def generate_place_info(request):
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
                    "detailsUrl": "",
                }
            }
        )
    
    context = {
        'places': places_geojson
    }

    return render(request, 'index.html', context)


def get_place_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    place_parameters = {
        "title": place.title,
        "imgs": [img.url.url for img in place.place_images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude, "lat": place.latitude}
    }

    return JsonResponse(
        place_parameters,
        safe=False,
        json_dumps_params={"ensure_ascii": False,
        "indent": 4}
        
    )