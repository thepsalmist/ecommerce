from django.urls import path
from . import views
from .views import shopping_cart

app_name = "cart"

urlpatterns = [
    path("", views.shopping_cart, name="shopping_cart"),
]
