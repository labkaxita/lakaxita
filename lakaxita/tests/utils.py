import urllib2
from functools import wraps

from django.test import TestCase
from django.contrib.sites.models import Site

import oembed

from lakaxita.attachments.oembed_providers import InternalAttachmentProvider


def is_valid_response(url):
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return False
    else:
        if response.getcode() is not 200:
            return False
    return True


class TestCase(TestCase):
    def assertQuerysetEqual(self, *args, **kwargs):
        if not kwargs.has_key('transform'):
            kwargs['transform'] = lambda obj: obj
        super(TestCase, self).assertQuerysetEqual(*args, **kwargs)

    def fake_oembed_site(self):
        site = Site.objects.get_current()
        site.domain = 'localhost:8000'
        site.save()

        oembed.site = oembed.sites.ProviderSite()
        oembed.site.register(InternalAttachmentProvider)


    @staticmethod
    def skipIfNotValidResponse(*urls):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                for url in urls:
                    attrs = url.split('.')
                    obj = self
                    for attr in attrs:
                        if hasattr(obj, attr):
                            obj = getattr(obj, attr)
                        else:
                            obj = url
                    url = obj
                    if not is_valid_response(url):
                        self.skipTest('can not get {}'.format(url))
                return func(self, *args, **kwargs)
            return wrapper
        return decorator
