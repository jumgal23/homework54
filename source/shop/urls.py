from django.urls import path,reverse
from .views import (products_view, product_view, category_add_view, product_add_view,
                    categories_view, category_edit_view, product_edit_view, delete_view)

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/<int:pk>/', product_view, name='product_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', product_add_view, name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit_view'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit_view'),
    path('products/<int:pk>/delete/', delete_view, name='delete_view'),
]


def get_absolute_url(self):
    return reverse('product_view', args=[str(self.id)])