from .models import ArticleTopic, ArticleLike, CollectionLike, ArticleCollection, AuthorLike


def add_topics_likes(articles):
    for article in articles:
        article.topics = ArticleTopic.objects.filter(article=article)
        article.likes_count = ArticleLike.objects.filter(
            article=article).count()


def add_likes(collections):
    for collection in collections:
        collection.likes_count = CollectionLike.objects.filter(
            collection=collection).count()


def add_articles_likes(collections):
    for collection in collections:
        article_collections = ArticleCollection.objects.filter(
            collection=collection)
        articles = [ac.article for ac in article_collections]
        add_topics_likes(articles)
        collection.articles = article_collections
    add_likes(collections)


def add_likes_author(author, user):
    if author:
        author_likes = AuthorLike.objects.filter(author=author)
        author.likes_count = author_likes.count()
        author.user_liked = author_likes.filter(user=user).count() > 0


def filter_articles(request, queryset):
    query_params = request.GET
    p_filter = query_params.get('filter')
    p_query = query_params.get('query')

    if p_query:
        if not p_filter:
            queryset = queryset.filter(title__icontains=p_query)
        elif p_filter == 'topic':
            article_topics = ArticleTopic.objects.filter(
                topic__icontains=p_query)
            queryset = [at.article for at in article_topics]
        elif p_filter == 'author':
            queryset = queryset.filter(
                author__user__username__icontains=p_query)
    elif p_filter == 'liked':
        article_likes = ArticleLike.objects.filter(user=request.user)
        articles = [al.article for al in article_likes]
        queryset = articles

    return {
        'filtered_qs': queryset,
        'query_text': p_query if not p_filter else ''
    }


def filter_collections(request, queryset):
    query_params = request.GET
    p_filter = query_params.get('filter')
    p_query = query_params.get('query')

    if p_query:
        if not p_filter:
            queryset = queryset.filter(title__icontains=p_query)
        elif p_filter == 'creator':
            queryset = queryset.filter(
                creator__username__icontains=p_query)
    elif p_filter == 'liked':
        collection_likes = CollectionLike.objects.filter(user=request.user)
        collections = [cl.collection for cl in collection_likes]
        queryset = collections

    return {
        'filtered_qs': queryset,
        'query_text': p_query
    }


def filter_authors(request, queryset):
    query_params = request.GET
    p_filter = query_params.get('filter')
    p_query = query_params.get('query')

    if p_query:
        if not p_filter:
            queryset = queryset.filter(
                user__username__icontains=p_query)
    elif p_filter == 'liked':
        author_likes = AuthorLike.objects.filter(user=request.user)
        authors = [al.author for al in author_likes]
        queryset = authors

    return {
        'filtered_qs': queryset,
        'query_text': p_query
    }
