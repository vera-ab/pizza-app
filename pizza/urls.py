from django.urls import path, include
from .views import index

app_name = 'pizza'

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", index),
    #path("", include("products.urls", namespace="products")),
    #path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace="accounts")),
    #path('auth/', include('authentication.urls', namespace="auth")),
]