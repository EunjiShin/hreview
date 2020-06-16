from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from hyuzi.views import ProductList


App_name = 'hyuzi'

urlpatterns = [
    path('', views.main, name ='main'),
    path('store/', views.store, name='store'),
    path('store/product_list/<category_id>', views.product_list, name='category'),
    path('mypage/', views.mypage, name='mypage'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/add/<int:product_id>/', views.cart_remove, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='remove_cart'),
    path('best/', views.best, name='best'),
    path('custom/', views.custom, name='custom'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
