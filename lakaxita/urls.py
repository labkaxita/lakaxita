from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site
import oembed
oembed.autodiscover()

from lakaxita.views import BaseView, JSTemplateView
from lakaxita.api import api




urlpatterns = patterns('',
        url(r'^$', BaseView.as_view(), name='base'),
        url(r'^news/', include('lakaxita.news.urls', 
            namespace='news')),
        url(r'^gallery/', include('lakaxita.gallery.urls', 
            namespace='gallery')),
        url(r'^groups/', include('lakaxita.groups.urls', 
            namespace='groups')),
        url(r'^#/lost_found/', include('lakaxita.lost_found.urls', 
            namespace='lost_found')),
        url(r'^attachments/', include('lakaxita.attachments.urls', 
            namespace='attachments')),
        #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

        url(r'^oembed/', include('oembed.urls')),
        url(r'^badbrowser/', include('django_badbrowser.urls')),
        url(r'^admin/filebrowser/', include(site.urls)),
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^markitup/', include('markitup.urls')),

        url('^', include(api.urls)),
        url('^template/(?P<path>.+)/$', JSTemplateView.as_view(), name='template'),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
