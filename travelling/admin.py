from django.contrib import admin
from .models import Locations

class LocationsAdmin(admin.ModelAdmin):
  list_display = ["name","price","offer"]


admin.site.register(Locations,LocationsAdmin)
