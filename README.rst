基于Django与Ajax的搜索引擎
===================

基于Django,可以自定义的异步搜索

特性
-----------------------------------

- 使用的最新版本jQuery库
- 显示实时搜索结果


安装要求
-----------------------------------

- Python 2.6 或 Python 2.7
- `Django <http://www.djangoproject.com/>`_ >= 1.3
- `jQuery <http://jquery.com/>`_ >= 1.4.4

安装::
    
    easy_install django-ajax-search

接下来，添加`ajax_search` 到你的 `INSTALLED_APPS` 并包含css和js::

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        # Other apps here
        'ajax_search',
    )


搞定你的URL::

    urlpatterns = patterns('',
        # Other patterns go here
        url(r'^ajax_search/',include('ajax_search.urls')),
    )
