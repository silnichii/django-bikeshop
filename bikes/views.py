from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BikesSerializer

def details(request, bike_id):
    bike = Bikes.objects.get(id=bike_id)
    context = {
        "bike": bike
    }
    return render(request, "detail.html", context)


@api_view(['GET'])
def bikes_list(request):
    if request.method == 'GET':
        bikes = Bikes.objects.all()
        serializer = BikesSerializer(bikes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def bike_item(request, bike_id):
    try:
        bike = Bikes.objects.get(pk=bike_id)
    except Bikes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BikesSerializer(bike)
        return Response(serializer.data)

