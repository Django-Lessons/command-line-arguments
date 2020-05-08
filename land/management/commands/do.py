from django.core.management.base import BaseCommand
from django.apps import apps


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
        model_class = apps.get_model(
            app_label='land',
            model_name=model
        )
        model_class.objects.create(
            title=title,
            description=description
        )

    def list(self, model):
        model_class = apps.get_model(
            app_label='land',
            model_name=model
        )
        for p in model_class.objects.all():
            self.stdout.write(
                f"{model.capitalize()} {p.title} {p.description}"
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
            self.style.SUCCESS("Done! Success.")
        )
