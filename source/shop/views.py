from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, TypeArticle
from .forms import ArticleForm, TypeArticleForm


def products_view(request):
    articles = Article.objects.filter(stock__gt=0).order_by('type', 'name')
    return render(request, 'products_view.html', {'articles': articles})


def product_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'product_view.html', {'article': article})


def category_add_view(request):
    if request.method == 'POST':
        form = TypeArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = TypeArticleForm()
    return render(request, 'category_add_view.html', {'form': form})


def product_add_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect(product.get_absolute_url())
    else:
        form = ArticleForm()
    return render(request, 'product_add_view.html', {'form': form})


def categories_view(request):
    typearticles = TypeArticle.objects.all()
    return render(request, 'categories_view.html', {'typearticles': typearticles})


def category_edit_view(request, pk):
    typearticle = get_object_or_404(TypeArticle, pk=pk)
    if request.method == 'POST':
        form = TypeArticleForm(request.POST, instance=typearticle)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = TypeArticleForm(instance=TypeArticle)
    return render(request, 'category_edit_view.html', {'form': form})


def product_edit_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            product = form.save()
            return redirect(product.get_absolute_url())
    else:
        form = ArticleForm(instance=article)
    return render(request, 'product_edit_view.html', {'form': form, 'article': article})


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('products_view')

    return render(request, 'delete.html', {'article': article})