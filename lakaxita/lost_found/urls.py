from django.conf.urls.defaults import patterns, url

from lakaxita.lost_found.views import ItemList, ItemDetail, CreateNotification


urlpatterns = patterns('',
        url('^$', ItemList.as_view(), name='list'),
        url('^(?P<slug>(\w|\d|-)+)/$', ItemDetail.as_view(), name='detail'),
        url('^(?P<slug>(\w|\d|-)+)/notify$', CreateNotification.as_view(), 
            name='notify'),
)
