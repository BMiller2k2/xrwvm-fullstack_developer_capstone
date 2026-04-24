from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # how many empty rows to show
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "dealer_id", "type", "year")
    list_filter = ("type", "year")
    search_fields = ("name",)
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [CarModelInline]
# Register models here
