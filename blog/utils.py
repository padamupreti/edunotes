from .models import ArticleTopic, ArticleLike, CollectionLike, ArticleCollection


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
