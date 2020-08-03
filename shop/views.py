from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "shop/index.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "shop/featured.html"


class ProductListView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "shop/product.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        try:
            instance = Product.objects.get(slug=slug, available=True)
        except Product.MultipleObjectsReturned:
            instance = queryset.first()
        except:
            raise Http404("Product does not exist")
        return instance

