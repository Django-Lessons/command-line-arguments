from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Manage Products and Plans'

    def add_arguments(self, parser):
        parser.add_argument(
            'operation',
            help="Operation to perform",
            choices=(
                'create',
                'list',
                'delete',
                'update'
            )
        )
        parser.add_argument(
            'model',
            help="Model to operate onto",
            choices=(
                'product',
                'plan',
            )
        )

    def handle(self, *args, **options):
        op = options.get('operation')
        model = options.get('model')
        self.stdout.write(
            f"Doing {op}... on {model}"
        )
        self.stdout.write(
            self.style.SUCCESS("Done! Success")
        )
