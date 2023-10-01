from django.contrib import admin

from .models import (Author, Article, ArticleLike, ArticleTopic,
                     Collection, CollectionLike, ArticleCollection)

models_list = [Author, Article, ArticleLike, ArticleTopic,
               Collection, CollectionLike, ArticleCollection]

for m in models_list:
    admin.site.register(m)
