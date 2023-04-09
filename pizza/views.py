from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Category, Ingredient, Order

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    ing = Ingredient.objects.all()
    return HttpResponse('str([t.title for t in pizzas])')
