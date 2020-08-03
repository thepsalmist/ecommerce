from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
)

app_name = "shop"

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("featured/", ProductFeaturedListView.as_view(), name="featured"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "featured/<slug:slug>/",
        ProductFeaturedDetailView.as_view(),
        name="featured-detail",
    ),
]
