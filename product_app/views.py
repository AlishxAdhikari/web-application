from django.shortcuts import render, redirect
from .models import Products
from decimal import Decimal

def Home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        price = Decimal(price)
        product = Products(name=name, price=price)
        product.save()
        return redirect("home")  # define product_list URL

    return render(request, "home.html")