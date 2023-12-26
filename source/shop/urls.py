from django.urls import path,reverse
from .views import (ProductsListView, ProductDetailView, category_add_view, ProductCreateView,
                    categories_view, category_edit_view, ProductUpdateView, ProductDeleteView)

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit_view'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_view'),
]


def get_absolute_url(self):
    return reverse('product_view', args=[str(self.id)])

