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
