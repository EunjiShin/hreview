from django.contrib import admin
from .models import User, Category, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


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