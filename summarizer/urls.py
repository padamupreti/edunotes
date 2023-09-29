from django.urls import path

from .views import home, create_summary, list_summaries

app_name = 'summarizer'
urlpatterns = [
    path('', home, name='home'),
    path('create-summary/', create_summary, name='create-summary'),
    path('list-summaries/', list_summaries, name='list-summaries'),
]
