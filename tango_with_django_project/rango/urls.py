
""" imports the relevant Django machinery that we use to
create URL mappings. """

from django.conf.urls import patterns, url
""" importing the views module from rango provides us with access to our simple view, allowing us to reference the view in the URL mapping we created """

from rango import views

""" Mappings (URLs) must be a tuple.
    For Django to pick your mappings up, this tuple must be
    named urlpatterns """

""" The url provided below url()--> contains a regex as
    one of the arguments...this maps to an empty string
    which will take you to the index page"""
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       )


