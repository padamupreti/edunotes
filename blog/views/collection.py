from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from datetime import date

from ..forms import CollectionForm
from ..models import Collection, CollectionLike, ArticleCollection
from ..utils import add_likes, add_articles_likes, filter_items


@login_required
def create_collection(request):
    form = CollectionForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            collection = form.save(commit=False)
            articles = form.cleaned_data.get('articles')
            collection.creator = request.user
            collection.save()
            for article in articles:
                ArticleCollection.objects.create(
                    article=article, collection=collection)
            return redirect('blog:list-user-collections')

    context = {
        'form': form
    }

    return render(request, 'blog/edit-collection.html', context)


def list_collections(request):
    collections = Collection.objects.all().order_by('-created_on')
    info = filter_items(request, collections)
    collections = info['filtered_qs']
    add_likes(collections)

    context = {
        'collections': collections,
        'query_text': info['query_text'],
        'show_creator': True
    }

    return render(request, 'blog/list-collections.html', context)


@login_required
def list_user_collections(request):
    collections = Collection.objects.filter(
        creator=request.user).order_by('-created_on')
    info = filter_items(request, collections)
    collections = info['filtered_qs']
    add_likes(collections)

    context = {
        'collections': collections,
        'query_text': info['query_text'],
        'show_creator': False
    }

    return render(request, 'blog/list-user-collections.html', context)


def collection_detail(request, pk):
    collection = get_object_or_404(Collection, id=pk)
    collections = Collection.objects.filter(
        creator=collection.creator).exclude(id=collection.id).order_by('-created_on')
    add_articles_likes([collection])
    collection.user_liked = CollectionLike.objects.filter(
        user=request.user, collection=collection).count() > 0
    add_likes(collections)

    context = {
        'collection': collection,
        'articles': [ac.article for ac in collection.articles],
        'show_author': True,
        'collections': collections[:3],
        'show_creator': True
    }

    return render(request, 'blog/collection-detail.html', context)


@login_required
def update_collection(request, pk):
    collections = Collection.objects.filter(creator=request.user)
    collection = get_object_or_404(collections, id=pk)
    article_collections = ArticleCollection.objects.filter(
        collection=collection).select_related('article')
    form = CollectionForm(request.POST or None, instance=collection, initial={
        'articles': [ac.article for ac in article_collections]
    })

    if request.method == 'POST':
        if form.is_valid():
            collection = form.save(commit=False)
            collection.updated_on = date.today()
            collection.save()
            articles = form.cleaned_data.get('articles')
            to_delete = [ac for ac in ArticleCollection.objects.filter(
                collection=collection) if ac.article not in articles]
            for ac in to_delete:
                ac.delete()
            for article in articles:
                ArticleCollection.objects.get_or_create(
                    article=article, collection=collection)
            return redirect('blog:collection-detail', pk=collection.id)

    context = {
        'form': form
    }

    return render(request, 'blog/edit-collection.html', context)


@login_required
def delete_collection(request, pk):
    collections = Collection.objects.filter(creator=request.user)
    collection = get_object_or_404(collections, id=pk)

    if request.method == 'POST':
        collection.delete()
        return redirect(reverse_lazy('blog:list-user-collections'))

    add_likes([collection])

    context = {
        'collection': collection
    }

    return render(request, 'blog/delete-collection.html', context)
