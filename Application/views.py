from django.shortcuts import render, redirect
from .forms import HouseForm
from django.http import JsonResponse
from .models import House
from django.contrib.auth.decorators import login_required

def wells_geojson(request):
    features = []

    for house in House.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(house.longitude), float(house.latitude)],
            },
            "properties": {
                "address": house.address,
                "owner_name": house.owner_name,
                "contact_number": house.contact_number,
                "well_depth": float(house.well_depth),
                "well_diameter": float(house.well_diameter),
                "water_ph": float(house.water_ph) if house.water_ph is not None else None,
                "is_potable": house.is_potable,
                "daily_yield": float(house.daily_yield) if house.daily_yield is not None else None,
                "notes": house.notes,
                "created_at": house.created_at.isoformat(),
                "updated_at": house.updated_at.isoformat(),
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson)


def add_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'house_success.html')  # Styled success page
    else:
        form = HouseForm()
    return render(request, 'house_form.html', {'form': form})


def house_success(request):
    return render(request, 'house_success.html')

@login_required(login_url='/admin/login/')
def home(request):
    return render(request, 'index.html')


