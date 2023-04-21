from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm
from .models import Pizza, Ingredient, Order


# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    ing = Ingredient.objects.all()
    return render(request, 'index.html', context={'pizzas': pizzas, 'ingrid': ing})


class PizzaList(TemplateView):
    template_name = "pizza_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pizzas_all = Pizza.objects.all()
        pizzas = pizzas_all.filter(is_custom=False)
        return {'pizzas': pizzas}


class CustomCreateView(CreateView):
    model = Pizza
    fields = ['title', 'ingredients', 'is_custom', ]
    template_name = 'custom-pizza.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return redirect('/custom-pizza-list/')

    def get_success_url(self):
        return reverse_lazy('/custom-pizza-list/')


class CustomPizzaList(TemplateView):
    template_name = "custom-pizza-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pizzas_all = Pizza.objects.all()
        pizzas = pizzas_all.filter(is_custom=True)
        return {'pizzas': pizzas}


class OrderCreateView(FormView):
    form_class = OrderForm
    template_name = 'order-create.html'
    success_url = "/"

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return super().form_valid(form)


