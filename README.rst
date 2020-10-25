========================
 Django Makeallmessages
========================

.. image:: https://img.shields.io/pypi/l/django-makeallmessages.svg
   :target: https://raw.githubusercontent.com/vonNiklasson/django-makeallmessages/develop/LICENSE

.. image:: https://img.shields.io/pypi/v/django-makeallmessages.svg
    :target: https://pypi.python.org/pypi/django-makeallmessages/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/wheel/django-makeallmessages.svg
    :target: https://pypi.python.org/pypi/django-makeallmessages/
    :alt: Supports Wheel format

.. role:: code(code)
.. role:: bash(code)
   :language: bash
.. role:: python(code)
   :language: python

Django Makeallmessages allows you to set default parameters to your :code:`makemessage` commands and covers all
the regular file extensions, including your JavaScript files, with one command!

**Instead of doing this**

.. code-block:: bash

    $ python manage.py makemessages --locale=en
                                    --locale=fr
                                    --ignore=tests/*
    $ python manage.py makemessages --locale=en
                                    --locale=fr
                                    --ignore=node_modules/*
                                    --ignore=tests/*
                                    --domain=djangojs

**Just do this**

.. code-block:: bash

    $ python manage.py makeallmessages

Requirements
============

Django Makeallmessages requires :code:`Django 2.2` or later.


Fetching It
===========

You can get Django Makeallmessages by using pip

.. code-block:: bash

    $ pip install django-makeallmessages

To install it from source, clone the repository and run :bash:`setup.py`

.. code-block:: bash

    $ git clone git://github.com/vonNiklasson/django-makeallmessages.git
    $ cd django-makeallmessages
    $ python setup.py install


Installation
============

To add :code:`django_makeallmessages` to your project you must first add it to :code:`INSTALLED_APPS` in the projects :code:`settings.py`
file

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_makeallmessages',
        ...
    )


Configuration
=============

TBA


Command Line Parameters
=======================

TBA

