from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import oembed
oembed.autodiscover()


urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='base.yammy'), name='base'),
        url(r'^groups/', include('lakaxita.groups.urls', 
            namespace='groups')),
        url(r'^lost_found/', include('lakaxita.lost_found.urls', 
            namespace='lost_found')),
        url(r'^attachments/', include('lakaxita.attachments.urls', 
            namespace='attachments')),

        url(r'^oembed/', include('oembed.urls')),
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^feedback/', include('feedback.urls')),
        url(r'^badbrowser/', include('django_badbrowser.urls')),
        #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
