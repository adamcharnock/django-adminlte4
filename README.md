AdminLTE Templates, Template Tags, and Admin Theme for Django
=============================================================

[![pypi_badge](https://badge.fury.io/py/django-adminlte4.png)](pypi.python.org/pypi/django-adminlte4)

Django AdminLTE2 provides the functionality of the AdminLTE2 theme
to developers in the form of standard base templates. Optional styling for
Django's built-in admin interface is also provided.

Installation
------------

Installation using pip:

    pip install django-adminlte2

Add to installed apps:

    INSTALLED_APPS = [
        'django_adminlte',

        ...
    ]

Usage
-----

The [base template] is designed to be highly customisable. Template blocks are provided to
allow you to hook in customisations as you wish

### Admin Theme Usage

Install as per the above installation instructions. The django admin UI should then change as expected.

Documentation
-------------

TODO

Credits
-------

This project a based heavily on work by the following:

* my previous project of [django_adminlte2], then prior to that...
* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]

  [django_adminlte2]: https://github.com/adamcharnock/django-adminlte2
  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
  [base template]: https://github.com/adamcharnock/django-adminlte4/blob/master/django_adminlte/templates/adminlte/base.html
