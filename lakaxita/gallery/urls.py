from django.conf.urls.defaults import patterns, url

from lakaxita.gallery.views import CategoryList, CategoryDetail


urlpatterns = patterns('',
        url('^$', CategoryList.as_view(), name='list'),
        url('^(?P<slug>(\w|\d|-)+)/$', CategoryDetail.as_view(), name='detail'),
)
