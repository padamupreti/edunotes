from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from datetime import date


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)], blank=True, null=True, default=None)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    published_on = models.DateField(default=date.today)
    updated_on = models.DateField(blank=True, null=True, default=None)
    content = RichTextField()
    content_summary = models.TextField()

    def __str__(self):
        if self.author:
            return f'{self.title} by {self.author}'
        return f'{self.title} by Deleted User'


class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}_likes_{self.article}'


class ArticleTopic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    topic = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.article}_topic_{self.topic}'


class Collection(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(default=date.today)
    updated_on = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.title}_created_by_{self.creator}'


class CollectionLike(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}_likes_{self.collection}'


class ArticleCollection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.collection}_article_{self.article}'
