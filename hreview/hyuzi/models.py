from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils import timezone

 
class UserManager(BaseUserManager):    
    use_in_migrations = True    
    
    def create_user(self, email, nickname, username, address=None, phone=None, password=None):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname,
            username = username,
            address = address,
            phone = phone,        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     

    def create_superuser(self, email, nickname, username, address, phone, password):       
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,  
            username = username,
            address = address,
            phone = phone,       
            password=password       
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 


class User(AbstractBaseUser,PermissionsMixin):    
    objects = UserManager()
    email = models.EmailField(max_length=255,unique=True)    
    nickname = models.CharField(max_length=100,null=False, unique=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    address = models.CharField(max_length=300, blank=True, unique=True)
    phone=models.CharField(max_length=11, blank=True, unique=True)     
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email', 'nickname', 'address', 'phone']


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
