from django_makeallmessages.settings import DEFAULT_VALUES
from django.core.management.commands.makemessages import Command as MakeMessagesCommand


class Command(MakeMessagesCommand):
    help = (
        "Run makemessages for all domains with optional default parameters read from MAM_DEFAULT in "
        "the projects settings.py file. For help on how to configure the default values, please consult "
        "https://github.com/vonNiklasson/django-makeallmessages\n\n"
        "Will ignore the domain parameter."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-mam-default', action='store_true', dest='no_mam_default',
            help="Ignore the declared default values set in MAM_DEFAULT in the projects settings file.",
        )
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        options, error = self.get_default_values(**options)

        if error:
            self.stderr.write('Default values contained errors. Aborting.')
            return

        # Copy the options argument to later on modify them
        options_django = options.copy()
        options_djangojs = options.copy()

        # Set the domain to django and djangojs
        options_django.update({'domain': 'django'})
        options_djangojs.update({'domain': 'djangojs'})

        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('django'))
        super(Command, self).handle(*args, **options_django)

        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('djangojs'))
        super(Command, self).handle(*args, **options_djangojs)

    def get_default_values(self, **options):
        error = False

        if isinstance(DEFAULT_VALUES['locale'], list):
            options = self.assert_value(options, 'locale', [])
            options['locale'] += DEFAULT_VALUES['locale']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.locale" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['extension'], list):
            options = self.assert_value(options, 'extensions', [])
            options['extensions'] += DEFAULT_VALUES['extension']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.extension" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['ignore'], list):
            options = self.assert_value(options, 'ignore', [])
            options['ignore_patterns'] += DEFAULT_VALUES['ignore']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.ignore" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['no_wrap'], bool):
            options['no_wrap'] = DEFAULT_VALUES['no_wrap']
        elif DEFAULT_VALUES['no_wrap'] is not None:
            self.stderr.write('Setting "MAM_DEFAULT.no_wrap" must be of type bool.')
            error = True

        return options, error

    @staticmethod
    def assert_value(obj, key, default_value):
        """
        Make sure that an object obj contains a key. If not, set obj[key] = default_value

        @param obj: The object to check on.
        @param key: The key to check if it exists.
        @param default_value: The value to set if the key doesn't exist on the object.
        @return: The obj instance, with the possibility that it's now modified.
        """
        if key in obj and obj[key] is None:
            obj[key] = default_value
        elif key not in obj:
            obj[key] = default_value
        return obj
