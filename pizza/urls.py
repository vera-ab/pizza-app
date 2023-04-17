from django.urls import path, include
from .views import index, PizzaList, CustomCreateView

app_name = 'pizza'

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", PizzaList.as_view(), name="pizza-list"),
    path('custom-pizza/', CustomCreateView.as_view(), name="custom-pizza"),
    #path("", include("products.urls", namespace="products")),
    #path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace="accounts")),
    #path('auth/', include('authentication.urls', namespace="auth")),
]