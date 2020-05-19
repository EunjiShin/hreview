import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import User, Category, Product
from django.views.generic import ListView

def main(request):
    return render(request, 'hyuzi/main.html')

def store(request):
    categories = Category.objects.all()
    return render(request, 'hyuzi/store_wig.html', {'categories':categories})

def allProduct(request, c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page)
    else:
        products = Products.objects.all()
    return render(request, 'hyuzi/store_wig.html', {'category':c_page, 'products':products})



