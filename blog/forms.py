from django import forms

from .models import Article, Collection, Author


class ArticleForm(forms.ModelForm):
    topics = forms.CharField(required=False)

    class Meta:
        model = Article
        fields = ['title', 'topics', 'content']


class CollectionForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        widget=forms.SelectMultiple(attrs={'multiple': ''}),
        label='Articles (Hold Ctrl or Command to select multiple)')

    class Meta:
        model = Collection
        fields = ['title', 'description', 'articles']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['description']
