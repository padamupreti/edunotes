from .models import ArticleTopic, ArticleLike


def add_topics_likes(articles):
    for article in articles:
        copy = article
        article.topics = ArticleTopic.objects.filter(article=copy)
        article.likes_count = ArticleLike.objects.filter(
            article=copy).count()
