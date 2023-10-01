from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'blog/home.html', context={})


@login_required
def create_article(request):
    return render(request, 'blog/create-article.html', context={})


@login_required
def list_articles(request):
    return redirect('blog:create-article')
