django-staticfiles-bootstrap
============================
Introducing Twitter Bootsrap to Django!


Usage
-----
This application is meant to be used with `django-staticfiles`_ which is now 
part of Django (since 1.3) as `django.contrib.staticfiles`_.  Make sure that 
staticfiles is properly setup and configured, then install this application using
`pip`_:

::

    pip install django-staticfiles-bootstrap

Finally, make sure that `bootstrap` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

    INSTALLED_APPS += ['bootstrap', ]

The less and original (non-concatenated) JavaScript files are included along 
with the compressed CSS files and concatenated and compressed JavaScript
files.


Build
-----
To build this, you need to have the `jshint`, `recess` and `uglify-js` 
installed via `npm`. See ``support/build.py`` for more information on how data 
is transferred from the submodule to the Python package.


Credits
-------
Thanks to `Travis Swicegood`_ (`django-staticfiles-jquery`_) and `Ash Christopher`_ 
(`django-bootstrap-static-files`_) for the inpiration.

.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _django.contrib.staticfiles: https://docs.djangoproject.com/en/dev/howto/static-files/#using-django-contrib-staticfiles
.. _pip: http://www.pip-installer.org/
.. _Travis Swicegood: https://github.com/tswicegood
.. _Ash Christopher: https://github.com/ashchristopher
.. _django-staticfiles-jquery: http://pypi.python.org/pypi/django-staticfiles-jquery
.. _django-bootstrap-static-files: http://pypi.python.org/pypi/django-bootstrap-static-files
