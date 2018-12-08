from django.shortcuts import render

from bikes.models import Bikes, Types

def index(request):

    bikes = Bikes.objects.order_by("type_name").filter(is_active=True)
    types = Types.objects.all()
    brands = Bikes.objects.values_list("brand", flat=True).distinct()

    # brand search
    if "brand" in request.GET:
        brand = request.GET["brand"]
        if brand:
            bikes = bikes.filter(brand__iexact=brand)

    # type search 
    if "type_name" in request.GET:
        type_name = request.GET["type_name"]
        if type_name:
            bikes = bikes.filter(type_name__name__iexact=type_name)

    # price search 
    if "price" in request.GET:
        price = request.GET["price"]
        if price == "2501":
            bikes = bikes.filter(price__gte=price)
        elif price != "":
            bikes = bikes.filter(price__lte=price)



    context = {
        "bikes": bikes,
        "types": types,
        "brands": brands,
        "values": request.GET
    }

    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")

