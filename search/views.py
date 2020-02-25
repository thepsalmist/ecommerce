from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Product


class SearchProductView(ListView):
    template_name = "shop/search.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get("q", None)
        if query is not None:
            return Product.objects.filter(name__icontains=query)
        return Product.objects.all()

