from django.urls import path
import authapp.views as authapp
# from .views import products

app_name = 'authapp'
urlpatterns = [
    # path('', products, name='index'),
    # path('<int:pk>/', products, name='category'),
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('verify/<str:email>/<str:activation_key>/', authapp.verify, name='verify'),
]