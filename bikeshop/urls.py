from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("pages.urls")),
    path("bikes/", include("bikes.urls")),
    path("admin/", admin.site.urls),
    re_path("api/", include("bikes.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
