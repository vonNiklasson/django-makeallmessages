from django_makeallmessages.settings import IGNORE_PATTERNS
from django.core.management.commands.makemessages import Command as MakeMessagesCommand


class Command(MakeMessagesCommand):
    help = "Run makemessages for all domains. Will ignore the domain parameter."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        # Check that the default ignore patterns is not excluded
        if options['use_default_ignore_patterns']:
            # Make sure that the IGNORE_PATTERNS setting is valid before continuing
            if isinstance(IGNORE_PATTERNS, list):
                # Append the IGNORE_PATTERNS from django settings to the argument
                options['ignore_patterns'] += IGNORE_PATTERNS
            else:
                self.stderr.write('Setting MAM_IGNORE_PATTERNS is not of type List. Aborting.')

        # Copy the options argument to later on modify them
        options_django = options.copy()
        options_djangojs = options.copy()

        # Set the domain to django and djangojs
        options_django.update({'domain': 'django'})
        options_djangojs.update({'domain': 'django'})

        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('django'))
        super(Command, self).handle(*args, **options_django)

        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('djangojs'))
        super(Command, self).handle(*args, **options_djangojs)
