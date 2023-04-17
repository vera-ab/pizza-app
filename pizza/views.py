from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
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


class CustomCreateView(CreateView):
    model = Pizza
    fields = '__all__'
    template_name = 'custom-pizza.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return redirect('/')

    def get_success_url(self):
        return reverse_lazy('/')
