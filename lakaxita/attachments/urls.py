from django.conf.urls.defaults import patterns, url

from lakaxita.attachments.views import AttachmentDetail, FileRedirect


urlpatterns = patterns('',
        url('^(?P<slug>(\w|\d|-)+)/$', AttachmentDetail.as_view(), name='detail'),
        url('^file/(?P<slug>(\w|\d|-)+)/$', FileRedirect.as_view(), name='file'),
)
