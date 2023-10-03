from django.shortcuts import render

from ..models import Author, AuthorLike
from ..utils import filter_authors


def list_authors(request):
    authors = Author.objects.all()
    info = filter_authors(request, authors)
    authors = info['filtered_qs']
    for author in authors:
        author.likes_count = AuthorLike.objects.filter(author=author).count()

    context = {
        'authors': authors,
        'query_text': info['query_text']
    }

    return render(request, 'blog/list-authors.html', context)
