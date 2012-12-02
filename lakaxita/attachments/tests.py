from datetime import date
from django.utils import unittest
from django.test import Client
from django.db import models
from django.contrib.sites.models import Site

from milkman.dairy import milkman
from milkman.generators import random_image

from lakaxita.attachments.models import Attachment, File


class FileTestCase(unittest.TestCase):
    def setUp(self):
        self.att_file = File(name='photo', type='photo')
        self.att_file.file.name = random_image(self.att_file.file.field)
        self.att_file.save()

    def test_oembed_creation(self):
        self.assertEqual(self.att_file.oembed, self.att_file.get_oembed_url())
        self.assertEqual(
                self.att_file.get_oembed_url(), 
                'http://{domain}/attachments/file/{pk}/'.format(
                    domain=Site.objects.get_current().domain, pk=self.att_file.pk))

    def test_oembed_type(self):
        for choice, _ in self.att_file.type_choices:
            self.att_file.type = choice
            if choice == 'audio':
                self.assertEqual(self.att_file.oembed_type, 'video')
            else:
                self.assertEqual(self.att_file.oembed_type, choice)

    def tearDown(self):
        self.att_file.file.delete()
        self.att_file.delete()
