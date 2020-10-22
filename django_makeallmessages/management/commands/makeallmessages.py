from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings
from django_makeallmessages.settings import IGNORE_PATTERNS


class Command(BaseCommand):
    help = "Runs makemessages for all domains."

    def add_arguments(self, parser):

        parser.add_argument('--ignore',
                            type='str',
                            default=None,
                            nargs='?',
                            dest='ignore_patterns',
                            help='Ignore certain folders or files based on a comma separated list.'
                                 'Defaults to MAM_IGNORE_PATTERNS from project settings.'
                                 'Append with + to add to already defined ignore patterns.')

    def handle(self, *args, **options):
        locales_default = [locale[0] for locale in settings.LANGUAGES]

        management.call_command('makemessages', locale=locales_default, domain='django', ignore=IGNORE_PATTERNS)
        management.call_command('makemessages', locale=locales_default, domain='djangojs', ignore=IGNORE_PATTERNS)
