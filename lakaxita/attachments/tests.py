import urllib2
from datetime import date

from django.utils import unittest
from django.test import Client
from django.db import models
from django.conf import settings

from milkman.generators import random_image

from lakaxita.attachments.models import ExternalAttachment, InternalAttachment


def fake_oembed_site():
    from django.contrib.sites.models import Site
    import oembed
    from lakaxita.attachments.oembed_providers import InternalAttachmentProvider

    site = Site.objects.get_current()
    site.domain = 'localhost:8000'
    site.save()

    oembed.site = oembed.sites.ProviderSite()
    oembed.site.register(InternalAttachmentProvider)


class InternalAttachmentTestCase(unittest.TestCase):
    def setUp(self):
        fake_oembed_site()

        rand_image = random_image(models.FileField())
        self.attachment = InternalAttachment(file=rand_image)
        self.attachment.save()

    def test_oembed_creation(self):
        self.assertTrue(self.attachment.is_oembed_valid())
        self.assertEqual(self.attachment.oembed, 
                self.attachment.get_oembed_url())
        self.assertEqual(self.attachment.get_oembed_url(), 
                'http://{domain}/attachments/file/{slug}/'.format(
                    domain='localhost:8000', slug=self.attachment.slug))

    def test_metadata(self):
        self.assertEqual(self.attachment.title, self.attachment.file.filename)
        self.assertEqual(self.attachment.metadata['url'], self.attachment.oembed)
        self.assertEqual(self.attachment.type, 'photo')
        self.assertEqual(self.attachment.author, settings.ATTACHMENTS['author_name'])
        self.assertEqual(self.attachment.author_url, settings.ATTACHMENTS['author_url'])
        self.assertTrue('img' in self.attachment.html)


    def tearDown(self):
        self.attachment.file.delete()
        self.attachment.delete()


class ExternalAttachmentTestCase(unittest.TestCase):
    def setUp(self):
        arginano = 'http://youtu.be/27PJBU-WNzI'
        jaion = 'http://youtu.be/-auzpsG_aVI'
        for url in arginano, jaion:
            try:
                response = urllib2.urlopen(url)
            except urllib2.URLError:
                self.skipTest('can not get {}'.format(url))
            else:
                if response.getcode() is not 200:
                    self.skipTest('can not get {}'.format(url))

        self.arginano = ExternalAttachment(oembed=arginano)
        self.arginano.save()

        self.jaion = ExternalAttachment(oembed=jaion)
        self.jaion.save()

    def test_title(self):
        pass

    def test_ordering(self):
        self.arginano.creation = date(1, 1, 1)
        self.arginano.save()

        self.jaion.creation = date(1, 1, 2)
        self.jaion.save()

        self.assertEqual(list(ExternalAttachment.objects.all()), 
                [self.jaion, self.arginano])

    def tearDown(self):
        self.arginano.delete()
        self.jaion.delete()
