from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Package)
admin.site.register(Destination)
# admin.site.register(PackageSummary)
admin.site.register(Departure)
admin.site.register(Itinerary)
admin.site.register(Inclusion)
admin.site.register(Exclusion)
admin.site.register(Hotel)
admin.site.register(PackageImage)
admin.site.register(TourDestination)
# admin.site.register(PackageDetail)