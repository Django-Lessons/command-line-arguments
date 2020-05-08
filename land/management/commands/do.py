from django.core.management.base import BaseCommand
from land.models import Plan, Product


CREATE = 'create'
UPDATE = 'update'
LIST = 'list'
DELETE = 'delete'
PRODUCT = 'product'
PLAN = 'plan'


class Command(BaseCommand):
    help = 'Manage Products and Plans'

    def add_arguments(self, parser):
        parser.add_argument(
            'operation',
            help="Operation to perform",
            choices=(
                CREATE,
                LIST,
                DELETE,
                UPDATE
            )
        )
        parser.add_argument(
            'model',
            help="Model to operate onto",
            choices=(
                PRODUCT,
                PLAN,
            )
        )
        parser.add_argument(
            '--title',
        )
        parser.add_argument(
            '--description',
        )

    def create(self, model, title, description):
        if model == PRODUCT:
            Product.objects.create(
                title=title,
                description=description
            )
        if model == PLAN:
            Plan.objects.create(
                title=title,
                description=description
            )

    def list(self, model):
        if model == PRODUCT:
            for p in Product.objects.all():
                self.stdout.write(
                    f"Product {p.title} {p.description}"
                )

        if model == PLAN:
            for p in Plan.objects.all():
                self.stdout.write(
                    f"Plan {p.title} {p.description}"
                )

    def handle(self, *args, **options):
        op = options.get('operation')
        model = options.get('model')
        title = options.get('title')
        description = options.get('description')

        if op == CREATE:
            self.create(model, title, description)
        if op == LIST:
            self.list(model)

        self.stdout.write(
            self.style.SUCCESS("Done! Success")
        )
