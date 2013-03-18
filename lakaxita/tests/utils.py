import urllib2
from functools import wraps

from django.test import TestCase, LiveServerTestCase
from django.contrib.sites.models import Site
from django.core.management import call_command
from django.db import connections, DEFAULT_DB_ALIAS

import oembed
from selenium.webdriver.firefox.webdriver import WebDriver

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
    synced = False

    @classmethod
    def setUpClass(cls):
        """
        Prepare database:
        * Call syncdb to create tables for tests.models (since during
        default testrunner's db creation modeltranslation.tests was not in INSTALLED_APPS
        """
        super(TestCase, cls).setUpClass()
        if not TestCase.synced:
            # In order to perform only one syncdb
            TestCase.synced = True
            call_command('syncdb', verbosity=0, migrate=False, interactive=False,
                         database=connections[DEFAULT_DB_ALIAS].alias, 
                         load_initial_data=False)

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


class LiveServerTestCase(LiveServerTestCase, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(LiveServerTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(LiveServerTestCase, cls).tearDownClass()
