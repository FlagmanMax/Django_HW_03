from django.urls import path

from . import views
from .views import index, about


urlpatterns = [
    path("", index, name='index'),
    path("index/", index, name='index'),
    path("about/", about, name='about'),

    path('dice/<int:n>/', views.dice, name='dice'),
    path('heads_tails/<int:n>/', views.heads_tails, name='heads_tails'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('rand/<int:n>/', views.rand, name='rand'),
    path('all/<int:n>/', views.all, name='all'),

    path('view_all_articles/', views.view_all_articles, name='view_all_articles'),
    path('view_all_articles_by_author/<int:n>/', views.view_all_articles_by_author, name='view_all_articles_by_author'),
    path('view_article_by_id/<int:n>/', views.view_article_by_id, name='view_article_by_id'),
    path('view_all_authors/', views.view_all_authors, name='view_all_articles'),



    ]