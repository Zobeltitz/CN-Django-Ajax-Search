django-ajax-search
===================

A customizable AJAX-powered search for Django.

Features
-----------------------------------

- Works with the latest jQuery library version
- Displays instant search results as you type


Installation Requirements
-----------------------------------

- Python 2.6 or Python 2.7
- `Django <http://www.djangoproject.com/>`_ >= 1.3
- `jQuery <http://jquery.com/>`_ >= 1.4.4

To install::
    
    easy_install django-ajax-search

Next add `ajax-search` to your `INSTALLED_APPS` to include the related css/js::

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        # Other apps here
        'ajax-search',
    )

The jQuery and jQuery UI libraries are not included in the distribution but must be included
in your templates. See the example project for an example using these libraries from the
Google CDN.

Once installed you should add the urls to your root url patterns::

    urlpatterns = patterns('',
        # Other patterns go here
        url(r'^ajax-search/',include('ajax-search.urls')),
    )

Full documentation at http://django-ajax-search.readthedocs.org/
	
Additional Help/Support
-----------------------------------

You can find additional help or support on the mailing list: http://groups.google.com/group/django-ajax-search
