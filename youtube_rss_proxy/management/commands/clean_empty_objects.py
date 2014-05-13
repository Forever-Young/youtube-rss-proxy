from datetime import datetime, timedelta

from django.core.management import BaseCommand

from ...models import Rss


class Command(BaseCommand):
    help = "Clean empty objects"

    def handle(self, *args, **options):
        Rss.objects.filter(access_token__isnull=True).filter(created_at__lte=datetime.now() - timedelta(days=1)).delete()
