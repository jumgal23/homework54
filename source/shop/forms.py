from django import forms
from .models import Article, TypeArticle


class TypeArticleForm(forms.ModelForm):
    class Meta:
        model = TypeArticle
        fields = ['title', 'description']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description', 'type', 'price','stock' , 'image']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=255, required=True)
    phone = forms.CharField(label='Phone', max_length=20, required=True)
