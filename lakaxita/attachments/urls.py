from django.conf.urls.defaults import patterns, url

from lakaxita.attachments.views import AttachmentDetail, FileRedirect


def null_view(*args, **kwargs):
    pass


urlpatterns = patterns('',
        url('^(?P<slug>(\w|\d|-)+)/$', AttachmentDetail.as_view(), name='detail'),
        url('^file/(?P<pk>\d+)/$', FileRedirect.as_view(), name='file'),
)
