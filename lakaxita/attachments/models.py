from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError

import oembed
from oembed.consumer import OEmbedConsumer
from polymorphic import PolymorphicModel
from autoslug import AutoSlugField
from filebrowser.fields import FileBrowseField

oembed_consumer = OEmbedConsumer()


class Attachment(PolymorphicModel):
    class Meta:
        ordering = ('-creation',)

    oembed = models.CharField(max_length=100, verbose_name=_('oembed'))

    creation = models.DateTimeField(editable=False, auto_now=True)
    slug = AutoSlugField(populate_from='_slug', unique=True)

    @models.permalink
    def get_absolute_url(self):
        return 'attachments:detail', (), {'slug': self.slug}

    def clean(self):
        try:
            oembed.site.embed(self.oembed)
        except Exception, msg:
            raise ValidationError(msg)

    def is_oembed_valid(self):
        try:
            self.clean()
        except ValidationError:
            return False
        else:
            return True

    @property
    def metadata(self):
        if self.is_oembed_valid():
            return oembed.site.embed(self.oembed).get_data()
        else:
            return {}

    @property
    def title(self):
        if 'title' in self.metadata:
            return self.metadata['title']

    @property
    def author(self):
        if 'author' in self.metadata:
            return self.metadata['author']
        elif 'author_name' in self.metadata:
            return self.metadata['author_name']

    @property
    def author_url(self):
        if 'author_url' in self.metadata:
            return self.metadata['author_url']

    @property
    def html(self):
        try:
            return oembed_consumer.parse_text(self.oembed)
        except:
            return '<a src="{oembed}">{oembed}</a>'.format(oembed=self.oembed)

    @property
    def thumbnail(self):
        if 'thumbnail_url' in self.metadata:
            return self.metadata['thumbnail_url']
        elif 'thumbnail' in self.metadata:
            return self.metadata['thumbnail']


class ExternalAttachment(Attachment):
    class Meta:
        verbose_name = _('external attachment')
        verbose_name_plural = _('external attachments')

    def __unicode__(self):
        return self.title if self.title else self.oembed

    @property
    def type(self):
        return self.metadata['type']

    @property
    def _slug(self):
        return self.title if self.title else self.pk


class InternalAttachment(Attachment):
    class Meta:
        verbose_name = _('internal attachment')
        verbose_name_plural = _('internal attachments')

    types = {
            'Image': 'photo',
            'Document': 'rich',
            'Video': 'video',
            'Audio': 'audio',
            }

    file = FileBrowseField(max_length=200)

    def __unicode__(self):
        return self.file.filename

    @property
    def _slug(self):
        return self.file.filename

    def save(self, *args, **kwargs):
        super(InternalAttachment, self).save(*args, **kwargs)
        self.oembed = self.get_oembed_url()
        return super(InternalAttachment, self).save(*args, **kwargs)

    def get_oembed_url(self, ssl=False):
        return 'http{ssl}://{domain}{path}'.format(
                ssl=('s' if ssl else ''),
                domain=Site.objects.get_current().domain,
                path=reverse('attachments:file', kwargs={'slug': self.slug}),
                )

    @property
    def type(self):
        return self.types[self.file.filetype]

    @property
    def oembed_type(self):
        return 'video' if self.type == 'audio' else self.type

