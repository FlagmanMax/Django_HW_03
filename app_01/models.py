from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.translation import gettext as _

# Create your models here.

class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField(_("Date"), default=date.today)

    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    def __str__(self):
        return f'{self.full_name()}'

# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию
# False

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(_("Date"), default=date.today)
    category = models.CharField(max_length=100)
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} '

class Comment(models.Model):
    content = models.TextField()
    updated = models.DateField(_("Date"), default=date.today)
    published = models.DateField(_("Date"), default=date.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment: {self.content}'