from django.contrib import admin

from .models import (Author, AuthorLike, Article, ArticleLike, ArticleTopic,
                     Collection, CollectionLike, ArticleCollection)

models_list = [Author, AuthorLike, Article, ArticleLike, ArticleTopic,
               Collection, CollectionLike, ArticleCollection]

for m in models_list:
    admin.site.register(m)
