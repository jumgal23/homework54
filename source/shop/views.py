from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, TypeArticle
from .forms import ArticleForm, TypeArticleForm, SimpleSearchForm
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy


class ProductsListView(ListView):
    model = Article
    template_name = 'products_view.html'
    context_object_name = 'articles'
    paginate_by = 6
    form_class = SimpleSearchForm

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(stock__gt=0, name__icontains=query).order_by('type', 'name')
        else:
            return Article.objects.filter(stock__gt=0).order_by('type', 'name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form_class(self.request.GET)
        return context


# def products_view(request):
#     articles = Article.objects.filter(stock__gt=0).order_by('type', 'name')
#     return render(request, 'products_view.html', {'articles': articles})

class ProductDetailView(DetailView):
    model = Article
    template_name = 'product_view.html'
    context_object_name = 'article'


# def product_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'product_view.html', {'article': article})


def category_add_view(request):
    if request.method == 'POST':
        form = TypeArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = TypeArticleForm()
    return render(request, 'category_add_view.html', {'form': form})

class ProductCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'product_add_view.html'

    def form_valid(self, form):
        product = form.save()
        return super().form_valid(form)

# def product_add_view(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect(product.get_absolute_url())
#     else:
#         form = ArticleForm()
#     return render(request, 'product_add_view.html', {'form': form})


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



class ProductUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'product_edit_view.html'

    def form_valid(self, form):
        product = form.save()
        return super().form_valid(form)

# def product_edit_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             product = form.save()
#             return redirect(product.get_absolute_url())
#     else:
#         form = ArticleForm(instance=article)
#     return render(request, 'product_edit_view.html', {'form': form, 'article': article})


class ProductDeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('products_view')

# def delete_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         article.delete()
#         return redirect('products_view')
#
#     return render(request, 'delete.html', {'article': article})