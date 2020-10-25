from django_makeallmessages.settings import DEFAULT_VALUES
from django.core.management.commands.makemessages import Command as MakeMessagesCommand


class Command(MakeMessagesCommand):
    help = (
<<<<<<< HEAD
        "Run makemessages for all domains with optional default parameters read from \"MAM_DEFAULT\" in "
        "the projects settings.py file. For help on how to configure the default values, please consult \n"
=======
        "Run makemessages for all domains with optional default parameters read from MAM_DEFAULT in "
        "the projects settings.py file. For help on how to configure the default values, please consult "
>>>>>>> Added possibility for more dynamic default values
        "https://github.com/vonNiklasson/django-makeallmessages\n\n"
        "Will ignore the domain parameter."
    )

    def add_arguments(self, parser):
        parser.add_argument(
<<<<<<< HEAD
            '--no-mam-default', action='store_true', dest='no_mam_default',
            help="Ignore the declared default values set in MAM_DEFAULT in the projects settings file.",
        )
        parser.add_argument(
            '--quiet', '-q', action='store_true', dest='quiet',
            help="Disables output. Will still print fatal errors.",
        )
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        # Store the stdout function to be able to restore it later
        stdout_write = self.stdout.write

        # Suppress any output
        if options['quiet']:
            stdout_write = self.stdout.write
            self.stdout.write = self.noop_write

        # Check if we want to use default values
        if not options['no_mam_default']:
            options, error = self.get_default_values(**options)
            # If errors occurred, print error message.
            if error:
                self.stderr.write('Default values contained errors. Aborting.')
                return
        else:
            self.stdout.write("Skipping default values.")
=======
            '--no-mam-default', action='sture_true', dest='no_mam_default',
            help="Ignore the declared default values set in MAM_DEFAULT in the projects settings file.",
        )
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        options, error = self.get_default_values(**options)

        if error:
            self.stdout.write(self.style.ERROR('Default values contained errors. Aborting.'))
>>>>>>> Added possibility for more dynamic default values

        # Copy the options argument to later on modify them
        options_django = options.copy()
        options_djangojs = options.copy()

        # Set the domain to django and djangojs
        options_django.update({'domain': 'django'})
        options_djangojs.update({'domain': 'djangojs'})

        # Work with the django domain
        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('django'))
        super(Command, self).handle(*args, **options_django)

        # Work with the djangojs domain
        self.stdout.write('Processing domain', ending=' ')
        self.stdout.write(self.style.SUCCESS('djangojs'))
        super(Command, self).handle(*args, **options_djangojs)

<<<<<<< HEAD
        # Restore stdout
        if options['quiet']:
            self.stdout.write = stdout_write

=======
>>>>>>> Added possibility for more dynamic default values
    def get_default_values(self, **options):
        error = False

        if isinstance(DEFAULT_VALUES['locale'], list):
<<<<<<< HEAD
            options = self.assert_value(options, 'locale', [])
=======
>>>>>>> Added possibility for more dynamic default values
            options['locale'] += DEFAULT_VALUES['locale']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.locale" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['extension'], list):
<<<<<<< HEAD
            options = self.assert_value(options, 'extensions', [])
=======
>>>>>>> Added possibility for more dynamic default values
            options['extensions'] += DEFAULT_VALUES['extension']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.extension" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['ignore'], list):
<<<<<<< HEAD
            options = self.assert_value(options, 'ignore', [])
=======
>>>>>>> Added possibility for more dynamic default values
            options['ignore_patterns'] += DEFAULT_VALUES['ignore']
        else:
            self.stderr.write('Setting "MAM_DEFAULT.ignore" must be of type list or string.')
            error = True

        if isinstance(DEFAULT_VALUES['no_wrap'], bool):
            options['no_wrap'] = DEFAULT_VALUES['no_wrap']
<<<<<<< HEAD
        elif DEFAULT_VALUES['no_wrap'] is not None:
=======
        else:
>>>>>>> Added possibility for more dynamic default values
            self.stderr.write('Setting "MAM_DEFAULT.no_wrap" must be of type bool.')
            error = True

        return options, error

<<<<<<< HEAD
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

    def noop_write(self, msg='', style_func=None, ending=None):
        pass

=======
>>>>>>> Added possibility for more dynamic default values
