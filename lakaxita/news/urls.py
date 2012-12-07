from django.conf.urls.defaults import patterns, url

from lakaxita.news.views import NewsList, NewsDetail, NewsGroupDetail


urlpatterns = patterns('',
        url('^$', NewsList.as_view(), name='list'),
        url('^(?P<slug>(\w|\d|-)+)/$', NewsDetail.as_view(), name='detail'),
        url('^group/(?P<slug>(\w|\d|-)+)/$', NewsGroupDetail.as_view(), name='group'),
)
