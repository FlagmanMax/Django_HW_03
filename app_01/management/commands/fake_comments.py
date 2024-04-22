import random
from random import choices, choice
from django.core.management.base import BaseCommand
from app_01.models import Author, Article, Comment

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic,laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eumexpedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."

class Command(BaseCommand):
    help = "Generate fake comments for articles."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='number of Authors and Posts added')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')

        author_list = Author.objects.all()
        article_list = Article.objects.all()

        for i in range(1, count + 1):
            comment = Comment(
                content=''.join(choices(text, k=random.randint(5, 30))),
                author=random.choice(author_list),
                article=random.choice(article_list)
            )
            comment.save()


