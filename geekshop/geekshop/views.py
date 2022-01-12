from django.shortcuts import render
import json

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context=context)