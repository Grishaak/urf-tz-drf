from django.contrib import admin

from dishes.models import Food, FoodCategory

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategory)
