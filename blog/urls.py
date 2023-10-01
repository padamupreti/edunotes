from django.urls import path

from .views import home, create_article, list_articles

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('create-article/', create_article, name='create-article'),
    path('list-articles/', list_articles, name='list-articles'),
]
