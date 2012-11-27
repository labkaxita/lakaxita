from django.conf.urls.defaults import patterns, url

from lakaxita.attachments.views import FileRedirect


def null_view(*args, **kwargs):
    pass


urlpatterns = patterns('',
#        url('^$', ItemList.as_view(), name='list'),
#        url('^(?P<slug>(\w|\d|-)+)/$', ItemDetail.as_view(), name='detail'),
        url('^file/(?P<pk>\d+)/$', FileRedirect.as_view(), name='file'),
#        url('^file/(?P<pk>\d+)/$', null_view, name='file'),
)
