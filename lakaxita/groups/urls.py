from django.conf.urls.defaults import patterns, url

from lakaxita.groups.views import GroupList, GroupDetail


urlpatterns = patterns('',
        url('^$', GroupList.as_view(), name='list'),
        url('^(?P<slug>(\w|\d|-)+)/$', ItemGroup.as_view(), name='detail'),
)
