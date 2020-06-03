import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import User, Category, Product
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm

def main(request):
    return render(request, 'hyuzi/main.html')

def store(request):
    categories = Category.objects.all()
    return render(request, 'hyuzi/store_wig.html', {'categories':categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product_all = Product.objects.filter(category_id=category).all()
    page_numbers_range = 9
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(product_all,page_numbers_range)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'hyuzi/product_list.html',{'product_all':product_all, 'category':category, 'products':products, 'page_range':page_range, 'paginator':paginator })

def cart(request):
    return render(request, 'hyuzi/cart.html')

def mypage(request):
    return render(request, 'hyuzi/mypage.html')

def best(request):
    return render(request, 'hyuzi/best.html')
