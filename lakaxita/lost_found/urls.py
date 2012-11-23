from django.conf.urls.defaults import patterns, url

from lakaxita.lost_found.views import ItemList, ItemDetail


urlpatterns = patterns('',
        url('^$', ItemList.as_view(), name='list'),
        url('^(?P<slug>(\w|\d|-)+)/$', ItemDetail.as_view(), name='detail'),
)
