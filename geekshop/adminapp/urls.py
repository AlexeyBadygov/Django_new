from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [

    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    # path('users/create/', adminapp.UsersCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),


    path('categories/read/', adminapp.ProductCategoryView.as_view(), name='categories'),
    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),


    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    # path('products/read/category/<int:pk>/', adminapp.ProductView.as_view(), name='products'),


    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

]