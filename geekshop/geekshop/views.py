from django.shortcuts import render
import json

from mainapp.models import Product


def index(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context=context)