Getting started
===============

- Python 2.6 or Python 2.7
- `Django <http://www.djangoproject.com/>`_ >= 1.3
- `jQuery <http://jquery.com/>`_ >= 1.4.4

To install::
    
    easy_install django-ajax-search

Next add `ajax_search` to your `INSTALLED_APPS` to include the related css/js::

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        # Other apps here
        'ajax_search',
    )


Once installed you should add the urls to your root url patterns::

    urlpatterns = patterns('',
        # Other patterns go here
        url(r'^ajax_search/',include('ajax_search.urls')),
    )

Now that you're done with the setup, :doc:`configure your installation</config>`.
