from django.shortcuts import render
from .models import Bikes

def details(request, bike_id):

    bike = Bikes.objects.get(id=bike_id)

    context = {
        "bike": bike
    }

    return render(request, "detail.html", context)
