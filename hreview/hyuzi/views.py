import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import User, Category, Product, Cart, CartItem
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ObjectDoesNotExist

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

# def cart(request):
#     return render(request, 'hyuzi/cart.html')

def mypage(request):
    return render(request, 'hyuzi/mypage.html')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'hyuzi/cart.html', dict(cart_items = cart_items, total=total, counter=counter))

def best(request):
    return render(request, 'hyuzi/best.html')
