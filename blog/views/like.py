from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse

from ..models import Article, ArticleLike, Collection, CollectionLike, Author, AuthorLike

# TODO modularize functions in this file


@login_required
def like_article(request, pk):
    if request.method == 'GET':
        raise Http404
    article = get_object_or_404(Article, id=pk)
    article_like = ArticleLike.objects.filter(
        user=request.user, article=article)
    if article_like:
        article_like.delete()
        response_string = '''<button class="my-3 font-bold text-md hover:text-red-600">
        <i class="fa-regular fa-heart" ></i> Like
        </button>'''
    else:
        ArticleLike.objects.create(user=request.user, article=article)
        response_string = '''<button class="my-3 font-bold text-md text-red-600">
        <i class="fa-solid fa-heart" ></i> Liked
        </button>'''
    return HttpResponse(response_string)


@login_required
def like_collection(request, pk):
    if request.method == 'GET':
        raise Http404
    collection = get_object_or_404(Collection, id=pk)
    collection_like = CollectionLike.objects.filter(
        user=request.user, collection=collection)
    if collection_like:
        collection_like.delete()
        response_string = '''<button class="my-3 font-bold text-md hover:text-red-600">
        <i class="fa-regular fa-heart" ></i> Like
        </button>'''
    else:
        CollectionLike.objects.create(user=request.user, collection=collection)
        response_string = '''<button class="my-3 font-bold text-md text-red-600">
        <i class="fa-solid fa-heart" ></i> Liked
        </button>'''
    return HttpResponse(response_string)


@login_required
def like_author(request, pk):
    if request.method == 'GET':
        raise Http404
    author = get_object_or_404(Author, id=pk)
    author_like = AuthorLike.objects.filter(
        user=request.user, author=author)
    if author_like:
        author_like.delete()
        response_string = '''<button class="my-3 font-bold text-md hover:text-red-600">
        <i class="fa-regular fa-heart" ></i> Like
        </button>'''
    else:
        AuthorLike.objects.create(user=request.user, author=author)
        response_string = '''<button class="my-3 font-bold text-md text-red-600">
        <i class="fa-solid fa-heart" ></i> Liked
        </button>'''
    return HttpResponse(response_string)
