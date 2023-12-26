from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, TypeArticle, CartItem, Order, OrderItem
from .forms import ArticleForm, TypeArticleForm, SimpleSearchForm, CheckoutForm
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


class ProductDetailView(DetailView):
    model = Article
    template_name = 'product_view.html'
    context_object_name = 'article'



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


class ProductDeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('products_view')


def add_to_cart(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if article.stock > 0:
        cart_item, created = CartItem.objects.get_or_create(product=article)

        if cart_item.quantity < article.stock:
            cart_item.quantity += 1
            cart_item.save()

    referer = request.META.get('HTTP_REFERER')
    return redirect(referer if referer else 'products_view')


def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart_view.html', {'cart_items': cart_items, 'total_price': total_price})



# views.py
def remove_from_cart(request, pk):
    article = get_object_or_404(Article, pk=pk)
    cart_item = get_object_or_404(CartItem, product=article)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    user = request.user

    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=user)

        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if not cart_items.exists():
            messages.error(request, 'Your cart is empty.')
            return redirect('qwe')

        order = Order.objects.create(
            user=user,
            name=name,
            address=address,
            phone=phone
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )

        cart_items.delete()
        messages.success(request, 'Order placed successfully!')
        return redirect('products_view')

    return redirect('cart_view')

