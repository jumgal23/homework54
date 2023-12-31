from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TypeArticle(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Заголовок', unique=True)
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id}. {self.title}. {self.description}'

    def get_absolute_url(self):
        return reverse('category_edit_view', args=[str(self.id)])

class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    type = models.ForeignKey('shop.TypeArticle', on_delete=models.RESTRICT, verbose_name='Тип', related_name='articles')
    created_at = models.DateTimeField(verbose_name='Дата выполнения', auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    image = models.URLField(max_length=1000, verbose_name='Изображение')
    stock = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.id}. {self.description}. {self.name}'

    def get_absolute_url(self):
        return reverse('product_view', args=[str(self.id)])


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Article', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} - {self.quantity} units in the cart'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Article', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.quantity} '





