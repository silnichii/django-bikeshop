from django.contrib import admin
from bikes.models import Bikes, Types


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "brand", "price")
    list_display_links = ["title"]


admin.site.register(Bikes, UserAdmin)
admin.site.register(Types) 