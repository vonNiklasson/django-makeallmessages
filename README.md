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

Django Makeallmessages allows you to set default parameters to your `makemessage` commands and covers all
the regular file extensions, including your JavaScript files, with one command!

**Don't do this :x:**

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

**Do this! :white_check_mark:**

```shell script
$ python manage.py makeallmessages
```

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

TBA


## Command Line Parameters

TBA

