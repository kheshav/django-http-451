from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Clean all entries for http451'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('dump', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.ERROR('Command not yet implemented'))
