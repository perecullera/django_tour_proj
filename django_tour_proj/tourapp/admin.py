from django.contrib import admin
from tourapp.models import Apartment, Owner

# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
	pass
admin.site.register(Apartment, ApartmentAdmin)

class OwnerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Owner, OwnerAdmin)
