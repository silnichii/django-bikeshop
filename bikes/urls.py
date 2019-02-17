from django.urls import path
from . import views

urlpatterns = [
    path("<int:bike_id>", views.details),
    path("bikes/", views.bikes_list),
    path("bikes/<int:bike_id>", views.bike_item)
]