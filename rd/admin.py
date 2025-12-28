from django.contrib import admin

# Register your models here.
from .models import Location, Owner, SparePart

admin.site.register(Location)
admin.site.register(Owner)
admin.site.register(SparePart)
