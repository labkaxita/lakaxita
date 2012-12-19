from datetime import date
from django.utils import unittest
from django.test import Client
from django.db import models

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
        self.attachment.full_clean()
        self.assertEqual(self.attachment.oembed, 
                self.attachment.get_oembed_url())
        self.assertEqual(self.attachment.get_oembed_url(), 
                'http://{domain}/attachments/file/{slug}/'.format(
                    domain='localhost:8000', slug=self.attachment.slug))

    def test_type(self):
        self.assertEqual(self.attachment.file.filetype, 'Image')

    def test_oembed_type(self):
        pass

    def tearDown(self):
        self.attachment.file.delete()
        self.attachment.delete()


class ExternalAttachmentTestCase(unittest.TestCase):
    def setUp(self):
        self.arginano = ExternalAttachment(
                oembed='http://youtu.be/27PJBU-WNzI')
        self.arginano.save()

        self.jaion = ExternalAttachment(oembed='http://youtu.be/-auzpsG_aVI')
        self.jaion.save()

    def test_title(self):
        print(self.arginano.title)

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
