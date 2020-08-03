from django.shortcuts import render

from .models import Cart


def shopping_cart(request):
    cart_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 10
    for product in products:
        print(product.name)
        total += product.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, "cart/shopping_cart.html", context={})
