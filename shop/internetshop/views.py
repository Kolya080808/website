from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request, "index.html",{
        'products': products
                    })