from django.urls import path

from .views.general import home
from .views.article import create_article, list_articles, list_user_articles, article_detail, update_article, delete_article
from .views.collection import create_collection, list_collections, list_user_collections, collection_detail, update_collection, delete_collection
from .views.like import like_article, like_collection

app_name = 'blog'
urlpatterns = [
    # General
    path('', home, name='home'),
    # Article
    path('articles/create/', create_article, name='create-article'),
    path('articles/', list_articles, name='list-articles'),
    path('articles/me/', list_user_articles, name='list-user-articles'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
    path('articles/<int:pk>/update/', update_article, name='update-article'),
    path('articles/<int:pk>/delete/', delete_article, name='delete-article'),
    # Collection
    path('collections/create/', create_collection, name='create-collection'),
    path('collections/', list_collections, name='list-collections'),
    path('collections/me/', list_user_collections, name='list-user-collections'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail'),
    path('collections/<int:pk>/update/',
         update_collection, name='update-collection'),
    path('collections/<int:pk>/delete/',
         delete_collection, name='delete-collection'),
    # Likes
    path('like/articles/<int:pk>/', like_article, name='like-article'),
    path('like/collections/<int:pk>/', like_collection, name='like-collection')
]
