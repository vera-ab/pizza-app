from django.contrib import admin
from .models import Pizza, Ingredient, Category, Order


admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Order)
