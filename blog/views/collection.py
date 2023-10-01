from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import CollectionForm
from ..models import Collection, ArticleCollection


@login_required
def create_collection(request):
    form = CollectionForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            collection = form.save(commit=False)
            articles = form.cleaned_data.get('articles')
            collection.creator = request.user
            collection.save(), pk
            for article in articles:
                ArticleCollection.objects.create(
                    article=article, collection=collection)
            return redirect('blog:list-user-collections')

    context = {
        'form': form
    }

    return render(request, 'blog/edit-collection.html', context)


def list_collections(request):
    collections = Collection.objects.all()

    context = {
        'collections': collections
    }

    return render(request, 'blog/list-collections.html', context)


def list_user_collections(request):
    collections = Collection.objects.filter(creator=request.user)

    context = {
        'collections': collections
    }

    return render(request, 'blog/list-user-collections.html', context)


def collection_detail(request, pk):
    return redirect('blog:list-articles')


@login_required
def update_collection(request, pk):
    return redirect('blog:list-articles')


@login_required
def delete_collection(request, pk):
    return redirect('blog:list-articles')
