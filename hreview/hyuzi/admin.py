from django.contrib import admin
from . import models
from .models import Category, Product, User

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'username',
        'email',
        'address',
        'phone',
    )

    list_display_links = (
        'nickname',
        'username',
        'email',
        'address',
        'phone',
    )
# admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sold', 'description']
    list_editable = ['price', 'sold', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15

admin.site.register(Product, ProductAdmin)