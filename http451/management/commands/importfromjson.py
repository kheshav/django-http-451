from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Import resources to be blocked from json file"

    def add_arguments(self, parser):
        parser.add_argument('--file', help='Path of json file to be imported')

    def handle(self, *args, **options):
        if options['file'] is None:
            raise CommandError("File argument not specified")
        print("Command not yet implemented")
