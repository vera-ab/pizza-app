from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .models import Pizza, Category, Ingredient, Order

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    ing = Ingredient.objects.all()
    cats = Category.objects.all()
    return render(request, 'index.html', context={'pizzas': pizzas, 'ingrid': ing})


class PizzaList(TemplateView):
    template_name = "pizza_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pizzas = Pizza.objects.all()
        return {'pizzas': pizzas}
