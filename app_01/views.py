from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, get_object_or_404
import logging
from random import randint, choice, choices
from .models import Author, Article, Comment


# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'{request} index.html')
    context = {"title": "Мой сайт"}
    return render(request, "app_01/index.html", context)

def about(request):
    logger.info(f'{request} about.html')
    context = {"name": "Максим",
               "about": "я иногда таксист",
               "title": "Обо мне",
                }
    return render(request, "app_01/about.html", context)


def heads_tails(request, n):
    logger.info('page heads_tails started')

    value = ['Орел', 'Решка']

    context = {'title': "Орел и решка",
               'res': []
              }
    # n = int(request.GET.get('n', '5'))
    while n > 0:
        context['res'].append(choice(value))
        n -= 1

    return render(request, "app_01/game.html", context)


def dice(request, n):
    logger.info('page dice started')

    context = {'title': "Кости",
               'res': [],
               }
    while n > 0:
        context['res'].append(randint(1, 6))
        n -= 1

    return render(request, "app_01/game.html", context)


def rand(request, n):
    logger.info('page rand started')

    context = {'title': "Случайное число",
               'res': [],
               }
    while n > 0:
        context['res'].append(randint(0,100))
        n -= 1

    return render(request, "app_01/game.html", context)


def all(request, n):
    logger.info('page all_games started')

    value = ['Орел', 'Решка']

    context = {'title': "Все игры",
               'res_ht': [],
               'res_d': [],
               'res_r': [],
              }

    while n > 0:
        context['res_ht'].append(choice(value))
        context['res_d'].append(randint(1, 6))
        context['res_r'].append(randint(1, 100))
        n -= 1

    return render(request, "app_01/all.html", context)


def view_all_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles,
               'title': "Список статей",
               }
    return render(request, 'app_01/template_articles_list.html', context)


def view_all_articles_by_author(request, n):
    author = Author.objects.filter(pk=n).first()
    articles = Article.objects.filter(author_id=n)

    context = {'articles': articles,
               'title': f"Список статей автора {author.full_name()}",
               }
    return render(request, 'app_01/template_articles_list.html', context)


def create_author(request):
    form = Author()
    context = {'form': form,
               'title': "Добавление автора",
               }
    return render(request, 'template_regform.html', context)


def view_all_authors(request):
    context = {'authors': Author.objects.all(),
               'title': "Список всех авторов",
               }
    return render(request, 'app_01/template_authors_list.html', context)


def view_article_by_id(request, n):
    # article = Article.objects.filter(pk=n).first

    article = Article.objects.get(id=n)
    article.show_count += 1
    article.save()

    comments = []
    comments = Comment.objects.filter(article=article)

    context = {'article': article,
               'title': f'Статья ',
               'comments': comments
               }

    return render(request, 'app_01/template_article.html', context)
