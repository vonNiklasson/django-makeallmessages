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



Django Makeallmessages is a tool, designed to ease the message making in your Django project.

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

