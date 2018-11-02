from django.core.management.base import BaseCommand, CommandError
from http451.models import http451_URLS as http451_URLSModel


class Command(BaseCommand):
    help = 'Dump all entries registered for http451'

    def handle(self, *args, **options):
        print(list(http451_URLSModel.objects.all().values()))
