from django.contrib import admin
from shop.models import Article, TypeArticle, Order, OrderItem


admin.site.register(TypeArticle)
class TypeArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id', 'title']
    fields = ['id', 'title', 'description']


admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'type', 'created_at', 'price', 'image', 'stock']
    list_display_links = ['id', 'name', 'description']
    search_fields = ['id', 'name']
    fields = ['name', 'description', 'created_at', 'detailed_description']
    readonly_fields = ['created_at']

