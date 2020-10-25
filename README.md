# Django Makeallmessages

[![License][license_img]][license_target]
[![Latest PyPI version][pypi_version_img]][pypi_target]
[![Supports Wheel format][wheel_img]][wheel_target]

[license_target]: https://raw.githubusercontent.com/vonNiklasson/django-makeallmessages/develop/LICENSE
[license_img]: https://img.shields.io/pypi/l/django-makeallmessages.svg

[pypi_target]: https://pypi.python.org/pypi/django-makeallmessages/
[pypi_version_img]: https://img.shields.io/pypi/v/django-makeallmessages.svg

[wheel_target]: https://pypi.python.org/pypi/django-makeallmessages/
[wheel_img]: https://img.shields.io/pypi/wheel/django-makeallmessages.svg

Django Makeallmessages allows you to set default arguments to your `makemessage` commands and covers all
the regular file extensions, including your JavaScript files, with one command!

**:x: Don't do this**

```shell script
$ python manage.py makemessages --locale=en
                                --locale=fr
                                --ignore=tests/*
$ python manage.py makemessages --locale=en
                                --locale=fr
                                --ignore=node_modules/*
                                --ignore=tests/*
                                --domain=djangojs
```

**:white_check_mark: Do this!**

```shell script
$ python manage.py makeallmessages
```

## Overview

 1. [Requirements](#requirements)
 2. [Fetching it](#fetching-it)
 3. [Installation](#installation)
 4. [Available parameters](#available-parameters)
 5. [Command line arguments](#command-line-arguments)

## Requirements

Django Makeallmessages requires `Django 2.2` or later.


## Fetching It

You can get Django Makeallmessages by using pip

```shell script
$ pip install django-makeallmessages
```

To install it from source, clone the repository and run `setup.py`

```shell script
$ git clone git://github.com/vonNiklasson/django-makeallmessages.git
$ cd django-makeallmessages
$ python setup.py install
```


## Installation

To add `django_makeallmessages` to your project you must first add it to `INSTALLED_APPS`
in the projects `settings.py` file

```python
INSTALLED_APPS = (
    ...
    'django_makeallmessages',
    ...
)
```


## Configuration

You can configure default values to be used when running `makeallmessages`. This is done by setting
the `MAM_DEFAULT`in your projects `settings.py` file.

**Example**:
```python
MAM_DEFAULT = {
    "locale": ["en", "fr"],
    "extension": ["php", "twig"],
    "ignore": ["node_modules/*", "tests/*"],
    "no_wrap": True
}
```

The default settings are all derived from the arguments used in the standard `makemessages` command.

### Available parameters:

 - `locale` (list): A list locales you want to make messages from.
 - `extension` (list): A list of extensions you want to include, beyond the standard extensions (html,txt,py,js)
 - `ignore` (list): A list of files or directories to ignore matching a glob-style pattern.
 - `no_wrap` (bool): A boolean that decides whether to not break long message lines into several lines.

## Command line arguments

Two additional CLI arguments has been added to the `makeallmessages` apart from the default ones
derived from `makemessages`.

The `makeallmessages` command is derived from the default `makemessages`, which means that you can still use any arguments
that are valid for `makemessages` as well.

 - `--no-mam-default`: Will ignore any default values set in the `MAM_DEFAULT` setting.
 - `--quiet, -q`: Suppresses any output when running the command. Fatal errors will still be printed.

