from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class UsersListView(ListView):
    model = ShopUser
    template_name = "adminapp/users.html"
    context_object_name = 'objects'


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'админка/пользователи'
        return context


class ProductView(ListView):
    model = ProductCategory
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'


class ProductCategoryView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'


class ProductCategoryCreateView(CreateView):
    model = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:products')
    form_class = ProductCategoryEditForm
    # fields = '__all__'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')
    fields = '__all__'


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    context_object_name = 'product_to_delete'
    success_url = reverse_lazy('admin_staff:categories')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


class ProductCreateView(CreateView):
    model = ProductCategory
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_staff:products')


class ProductUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_staff:products')


class ProductDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/product_delete.html'
    context_object_name = 'product_to_delete'
    success_url = reverse_lazy('admin_staff:categories')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/cоздание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))

    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'user_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', context)

# class UsersCreateView(CreateView):
#     model = ShopUser
#     template_name = "adminapp/users.html"
#     # success_url = reverse_lazy('admin_staff:users')
#     form_class = ShopUserRegisterForm
#
#     # @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     # def dispatch(self, *args, **kwargs):
#     #     return super().dispatch(*args, **kwargs)
#     #
#     # def get_queryset(self):
#     #     return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     #
#     # def get_context_data(self, *, object_list=None, **kwargs):
#     #     context = super(UsersCreateView, self).get_context_data(**kwargs)
#     #     context['title'] = 'админка/пользователи'
#     #     return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:product_update', args=[edit_product.pk]))
#
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     context = {
#         'title': title,
#         'update_form': edit_form,
#         'category': edit_product.category
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': product,
#     }
#
#     return render(request, 'adminapp/product_delete.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'продукт/cоздание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
#
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     context = {
#         'title': title,
#         'update_form': product_form,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)
