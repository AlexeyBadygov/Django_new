from django.urls import path
from .views import products

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    # path('<int:pk>/', products, name='category'),
]