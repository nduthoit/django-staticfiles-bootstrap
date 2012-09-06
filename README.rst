django-staticfiles-bootstrap
============================
Introducing Twitter Bootsrap to Django!


Usage
-----
This application is meant to be used with `django-staticfiles`_.  Make sure
that staticfiles setup and configured, then install this application using
`pip`_:

::

    pip install django-staticfiles-bootstrap

Finally, make sure that `bootstrap` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

    INSTALLED_APPS += ['bootstrap', ]


Build
-----
To build this, you need to have the `jshint`, `recess` and `uglify-js` installed via `npm`.
See ``support/build.py`` for more information on how data is transferred from the submodule to the Python package.

.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/