from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from datetime import date

from ..forms import ArticleForm
from ..models import Article, ArticleTopic, Author
from ..utils import add_topics_likes


@login_required
def create_article(request):
    form = ArticleForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            (author, _) = Author.objects.get_or_create(user=request.user)
            article.author = author
            # TODO properly create content summary (huggingface transformers)
            article.content_summary = 'random words here TODO to change'
            article.save()
            input_topics = form.cleaned_data.get('topics')
            if input_topics:
                topic_strings = [t.strip() for t in input_topics.split(',')]
                for topic in topic_strings:
                    ArticleTopic.objects.create(article=article, topic=topic)
            return redirect('blog:list-user-articles')

    context = {'form': form}

    return render(request, 'blog/edit-article.html', context)


def list_articles(request):
    articles = Article.objects.all()
    add_topics_likes(articles)

    context = {
        'articles': articles
    }

    return render(request, 'blog/list-articles.html', context)


@login_required
def list_user_articles(request):
    articles = Article.objects.filter(author__user=request.user)
    add_topics_likes(articles)

    context = {
        'articles': articles
    }

    return render(request, 'blog/list-user-articles.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    articles = Article.objects.filter(
        author=article.author).exclude(id=article.id)
    add_topics_likes([article])
    add_topics_likes(articles)

    context = {
        'article': article,
        'other_articles': articles[:3]
    }

    return render(request, 'blog/article-detail.html', context)


@login_required
def update_article(request, pk):
    articles = Article.objects.filter(author__user=request.user)
    article = get_object_or_404(articles, id=pk)
    form = ArticleForm(request.POST or None, instance=article, initial={
        'topics': ', '.join([at.topic for at in ArticleTopic.objects.filter(article=article)])
    })

    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            # TODO properly create content summary (huggingface transformers)
            article.content_summary = 'random words here TODO to change'
            article.updated_on = date.today()
            article.save()
            input_topics = form.cleaned_data.get('topics')
            if input_topics:
                topic_strings = [t.strip() for t in input_topics.split(',')]
                to_delete = [at for at in ArticleTopic.objects.filter(
                    article=article) if at.topic not in topic_strings]
                for at in to_delete:
                    at.delete()
                for topic in topic_strings:
                    ArticleTopic.objects.get_or_create(
                        article=article, topic=topic)
            else:
                ArticleTopic.objects.filter(article=article).delete()
            return redirect('blog:list-user-articles')

    context = {'form': form}

    return render(request, 'blog/edit-article.html', context)


@login_required
def delete_article(request, pk):
    articles = Article.objects.filter(author__user=request.user)
    article = get_object_or_404(articles, id=pk)

    if request.method == 'POST':
        article.delete()
        return redirect(reverse_lazy('blog:list-user-articles'))

    add_topics_likes([article])

    context = {
        'article': article
    }

    return render(request, 'blog/delete-article.html', context)
