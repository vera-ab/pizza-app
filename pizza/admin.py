from django.contrib import admin
from .models import Pizza, Ingredient, Order


admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(Order)
