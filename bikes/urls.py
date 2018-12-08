from django.urls import path
from . import views

urlpatterns = [
    path("<int:bike_id>", views.details, name="details")
]