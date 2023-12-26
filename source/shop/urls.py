from django.urls import path,reverse
from .views import (ProductsListView, ProductDetailView, category_add_view, ProductCreateView,
                    categories_view, category_edit_view, ProductUpdateView, ProductDeleteView,
                    cart_view, add_to_cart, remove_from_cart, checkout)


urlpatterns = [
    path('', ProductsListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit_view'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_view'),
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),

]



def get_absolute_url(self):
    return reverse('product_view', args=[str(self.id)])



