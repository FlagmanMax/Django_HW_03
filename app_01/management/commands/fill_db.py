from random import choices, choice
from django.core.management.base import BaseCommand
from app_01.models import Author, Article

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
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='number of Authors and Posts added')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        set_published = [True, False]

        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                f_name=f'Name_{i}',
                l_name=f'Surname_{i}',
                email=f'author{i}@mail.ru',
                bio=f"Biography of Author_{i}: ".join(choices(text, k=64)),
            )
            author.save()


            for j in range(1, count + 1):
                article = Article(
                    title=f'Title_{i*100}_{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author,
                    category=" ".join(choices(text, k=2)),
                    is_published=choice(set_published)
                )
                article.save()

            print(author.f_name)