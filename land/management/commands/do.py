from django.core.management.base import BaseCommand
from django.apps import apps
from land.models import Product, Plan

CREATE = 'create'
LIST = 'list'
UPDATE = 'update'
DELETE = 'delete'
PRODUCT = 'product'
PLAN = 'plan'

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'operation',
            choices=(
                CREATE,
                LIST,
                UPDATE,
                DELETE
            )
        )
        parser.add_argument(
            'model',
            choices=(
                PRODUCT,
                PLAN,
            )
        )
        parser.add_argument(
            '-t', '--title', default="Default title"
        )
        parser.add_argument(
            '-d', '--description', default="Default description"
        )

    def get_model(self, model):
        return apps.get_model(
            app_label='land',
            model_name=model
        )

    def create(self, model, title, description):
        self.stdout.write(f"Creating {model}...")
        model_class = self.get_model(model)
        model_class.objects.create(
            title=title,
            description=description
        )

    def list(self, model):
        self.stdout.write(f"Listing {model}...")
        model_class = self.get_model(model)

        for item in model_class.objects.all():
            self.stdout.write(
                f"Product: title={item.title} descr={item.description}"
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

        if op in (CREATE, LIST, UPDATE, DELETE):
            self.stdout.write(
                self.style.SUCCESS("Done! Success.")
            )



