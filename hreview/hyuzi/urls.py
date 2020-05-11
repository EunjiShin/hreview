from django.urls import path
from . import views

App_name = 'hyuzi'


urlpatterns = [
    path('', views.main, name ='main'),
]