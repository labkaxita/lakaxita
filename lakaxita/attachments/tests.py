from __future__ import unicode_literals

from datetime import date

from django.utils import unittest
from django.test import TestCase, Client
from django.db import models
from django.conf import settings

from milkman.generators import random_image
from filebrowser.fields import FileObject
from filebrowser import signals

from lakaxita.tests.utils import TestCase
from lakaxita.attachments.models import ExternalAttachment, InternalAttachment


class InternalAttachmentTestCase(TestCase):
    def setUp(self):
        self.fake_oembed_site()
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


class InternalAttachmentSignalsTestCase(TestCase):
    def setUp(self):
        self.filename = 'random_name'
        self.file_obj = FileObject(self.filename)

    def test_create_signal(self):
        signals.filebrowser_post_upload.send(
                sender=None, path='', file=self.file_obj)
        attachments = InternalAttachment.objects.all()
        self.assertEqual(attachments.count(), 1)
        self.assertEqual(attachments[0].file.filename, self.filename)

    def test_rename_signal(self):
        new_name = 'some_other_name'
        attachment = InternalAttachment(file=self.filename)
        attachment.save()
        signals.filebrowser_post_rename.send(
                sender=None, path=self.file_obj.path, 
                name=self.file_obj.filename, new_name=new_name)
        attachments = InternalAttachment.objects.all()
        self.assertEqual(attachments.count(), 1)
        self.assertEqual(attachments[0].file.filename, new_name)

    def test_delete_signal(self):
        attachment = InternalAttachment(file=self.filename)
        signals.filebrowser_pre_delete.send(
                sender=None, path=self.file_obj.path, 
                name=self.file_obj.filename)
        self.assertEqual(InternalAttachment.objects.count(), 0)

    def tearDown(self):
        InternalAttachment.objects.delete()


class ExternalAttachmentTestCase(TestCase):
    def setUp(self):
        arginano = 'http://youtu.be/27PJBU-WNzI'
        jaion = 'http://youtu.be/-auzpsG_aVI'
        self.arginano = ExternalAttachment(oembed=arginano)
        self.arginano.save()
        self.jaion = ExternalAttachment(oembed=jaion)
        self.jaion.save()

    @TestCase.skipIfNotValidResponse('arginano.oembed', 'jaion.oembed')
    def test_metadata(self):
        self.assertEqual(self.arginano.title, 'Karlos Argui\xf1ano - Lakaxita gaztetxea')
        self.assertEqual(self.arginano.type, 'video')
        self.assertEqual(self.arginano.author, 'Lakaxita Gaztetxea')
        self.assertEqual(self.arginano.author_url, 'http://www.youtube.com/user/lakaxita')
        self.assertTrue('iframe' in self.arginano.html)

    def test_ordering(self):
        self.arginano.creation = date(1, 1, 1)
        self.arginano.save()
        self.jaion.creation = date(1, 1, 2)
        self.jaion.save()
        self.assertQuerysetEqual(ExternalAttachment.objects.all(),
                [self.jaion, self.arginano])

    def tearDown(self):
        self.arginano.delete()
        self.jaion.delete()


class AttachmentDetailTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.fake_oembed_site()
        rand_image = random_image(models.FileField())
        self.internal = InternalAttachment(file=rand_image)
        self.internal.save()

        external = 'http://youtu.be/-auzpsG_aVI'
        self.external = ExternalAttachment(oembed=external)
        self.external.save()

        self.responses = {
                self.internal: self.client.get(
                    self.internal.get_absolute_url(), follow=True),
                self.external: self.client.get(
                    self.external.get_absolute_url(), follow=True),
                }

    def test_status(self):
        for response in self.responses.values():
            self.assertEqual(response.status_code, 200)

    def test_template(self):
        for response in self.responses.values():
            self.assertTemplateUsed(response, 'attachments/attachment_detail.yammy')

    def test_context(self):
        for attachment, response in self.responses.items():
            self.assertEqual(response.context['attachment'], attachment)
