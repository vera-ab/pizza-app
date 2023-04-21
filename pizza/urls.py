from django.urls import path
from .views import PizzaList, CustomCreateView, CustomPizzaList, OrderCreateView

app_name = 'pizza'

urlpatterns = [
    path('', PizzaList.as_view(), name='pizza-list'),
    path('custom-pizza/', CustomCreateView.as_view(), name='custom-pizza'),
    path('custom-pizza-list/', CustomPizzaList.as_view(), name='custom-pizza-list'),
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
]
