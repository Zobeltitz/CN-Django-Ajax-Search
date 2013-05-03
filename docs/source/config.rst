Configuration
=============

The jQuery library is not included in the distribution but must be included
in your templates. Import it::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

Include the django-ajax-search media/static files to your project media/static folder. Then include the files in your templates. Make sure to use the correct path::
    
    <link rel="stylesheet" type="text/css" href="/media/ajax_search/css/ajax_search.css" />
    <script src="/media/ajax_search/js/ajax_search.js" type="text/javascript"></script>

Include global settings in your **settings.py** file.    
     
Specify the maximum number of instant-search results you'd like to see in the search drop-down menu::
    
    AJAX_SEARCH_LIMIT = 8

Specify the search helper function that we shall configure in a moment (use the full path)::
    
    AJAX_SEARCH_HELPER = 'app.views.search_helper'

Specify the search-results template where you'd like to see the results displayed. We shall configure it shortly::
    
    SEARCH_RESULT_TEMPLATE = 'search_results.html'

Import the search form in your views and pass it to templates::

    from ajax_search.forms import SearchForm
    
    return render_to_response(template_name, {'searchform':SearchForm()})

In your templates where you want to have the search form, include the code (make sure to keep **autocomplete off** and don't change the class and id of any tag if you wish to include formatting)::
    
    <form class="searchfield" method="get" action="/ajax_search/search/" autocomplete="off">
      {{ searchentryform.q }}
      <input id="searchbuttonmain" type="submit" class="subbtn" value="Search">
    </form>

Now that you've configured the basics, move on to the :doc:`Search Tools</searchtools>` section.
