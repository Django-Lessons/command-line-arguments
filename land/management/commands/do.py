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
            '-t', '--title',
        )
        parser.add_argument(
            '-d', '--description',
        )
        parser.add_argument(
            '--debug',
            action="store_true"
        )

    def create(self, model, title, description, verbose):
        if verbose:
            self.stdout.write(
                f"Creating {model}"
            )
        model_class = apps.get_model(
            app_label='land',
            model_name=model
        )
        model_class.objects.create(
            title=title,
            description=description
        )
        if verbose:
            self.stdout.write(
                "create complete"
            )

    def list(self, model, verbose):
        if verbose:
            self.stdout.write(
                f"listing {model}"
            )
        model_class = apps.get_model(
            app_label='land',
            model_name=model
        )
        for p in model_class.objects.all():
            self.stdout.write(
                f"{model.capitalize()} {p.title} {p.description}"
            )
        if verbose:
            self.stdout.write(
                "listing complete"
            )

    def handle(self, *args, **options):
        op = options.get('operation')
        model = options.get('model')
        title = options.get('title')
        description = options.get('description')
        verbose = options.get('debug')

        if op == CREATE:
            self.create(model, title, description, verbose)
        if op == LIST:
            self.list(model, verbose)

        self.stdout.write(
            self.style.SUCCESS("Done! Success.")
        )
