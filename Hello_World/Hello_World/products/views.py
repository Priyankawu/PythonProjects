
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def admin_console(request):
    products = Product.objects.all()   # object is the mgr that interacts with database
    render(request, "products/products_page.html", {'products': products})
