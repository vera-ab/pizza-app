from django.db import transaction
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView

from .forms import CustomPizzaForm, OrderForm
from .models import Pizza, Ingredient, Order
from .serializers import PizzaSerializer

from rest_framework.generics import (
    ListCreateAPIView,
)
class MyPizzaView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()



def index(request):
    pizzas = Pizza.objects.all()
    ing = Ingredient.objects.all()
    return render(request, 'index.html', context={'pizzas': pizzas, 'ingrid': ing})


class PizzaList(TemplateView):
    template_name = 'pizza_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzas'] = Pizza.objects.filter(is_custom=False)
        return context


class CustomCreateView(TemplateView):
    template_name = 'custom-pizza.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_pizza_form'] = CustomPizzaForm()
        context['order_form'] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        custom_pizza_form = CustomPizzaForm(self.request.POST)
        order_form = OrderForm(self.request.POST)

        if not custom_pizza_form.is_valid() or not order_form.is_valid():
            messages.warning(self.request, 'Pizza not created and order not created!')
            return redirect(reverse_lazy('pizza:custom-pizza'))

        custom_pizza_form_cleaned_data = custom_pizza_form.cleaned_data
        order_form_cleaned_data = order_form.cleaned_data

        # save all or nothing
        with transaction.atomic():
            # save pizza
            ingredients = custom_pizza_form_cleaned_data.pop('ingredients', [])
            new_pizza = Pizza.objects.create(is_custom=True, **custom_pizza_form_cleaned_data)
            new_pizza.ingredients.set(ingredients)
            new_pizza.save()
            # save order with pizza
            Order.objects.create(pizza=new_pizza, **order_form_cleaned_data)

        messages.success(self.request, 'Custom pizza and order successfully created.')
        return redirect(reverse_lazy('pizza:order-list'))


class CustomPizzaList(TemplateView):
    template_name = 'custom-pizza-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzas'] = Pizza.objects.filter(is_custom=True)
        return context


class OrderCreateView(FormView):
    form_class = OrderForm
    template_name = 'order-create.html'
    success_url = '/'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return super().form_valid(form)

class OrderListView(TemplateView):
    template_name = 'order-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context