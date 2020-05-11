import operator
from django.shortcuts import render, get_object_or_404, redirect
from .models import User

def main(request):
    return render(request, 'hyuzi/main.html')
