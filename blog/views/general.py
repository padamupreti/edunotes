from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models import Article, Collection, Author
from ..utils import add_topics_likes, add_likes, add_likes_author
from ..forms import AuthorForm

# TODO modularize the code below in home


def home(request):
    articles = Article.objects.all()
    add_topics_likes(articles)
    articles = sorted(articles, key=lambda a: a.likes_count, reverse=True)

    collections = Collection.objects.all()
    add_likes(collections)
    collections = sorted(
        collections, key=lambda c: c.likes_count, reverse=True)

    authors = Author.objects.all()
    for author in authors:
        add_likes_author(author, request.user)
    authors = sorted(authors, key=lambda a: a.likes_count, reverse=True)

    context = {
        'articles': articles[:3],
        'show_author': True,
        'collections': collections[:3],
        'show_creator': True,
        'authors': authors[:3]
    }

    return render(request, 'blog/home.html', context)


def author_profile(request, pk):
    author = get_object_or_404(Author, id=pk)

    articles = Article.objects.filter(author=author)
    add_topics_likes(articles)
    articles = sorted(articles, key=lambda a: a.likes_count, reverse=True)

    collections = Collection.objects.filter(creator=author.user)
    add_likes(collections)
    collections = sorted(
        collections, key=lambda c: c.likes_count, reverse=True)

    add_likes_author(author, request.user)

    context = {
        'author': author,
        'articles': articles[:3],
        'collections': collections[:3]
    }

    return render(request, 'blog/author-profile.html', context)


@login_required
def user_profile(request):
    (author, _) = Author.objects.get_or_create(user=request.user)
    add_likes_author(author, request.user)
    edit_form = AuthorForm(instance=author)

    if request.method == 'POST':
        post_data = request.POST
        if post_data.get('form_type') == 'edit_form':
            edit_form = AuthorForm(post_data, instance=author)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('.')
        else:
            author.user.delete()
            logout(request)
            return redirect('blog:home')

    context = {
        'author': author,
        'form': edit_form
    }

    return render(request, 'blog/author-profile.html', context)
