from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import resolve_url
from django.urls import reverse

# 유저
class User(AbstractUser): 
    profile  = models.ImageField()

# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


# 상품
class Product(models.Model):
    name = models.CharField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.IntegerField(blank=True, null=True)
    # media/image/에 저장됨
    image = models.ImageField(upload_to="image", blank=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return "["+self.category.name+"]"+self.name

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
