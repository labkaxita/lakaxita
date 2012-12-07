from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site

import oembed
from oembed.consumer import OEmbedConsumer
from polymorphic import PolymorphicModel
from autoslug import AutoSlugField

oembed_consumer = OEmbedConsumer()


class MetaAttachment(PolymorphicModel):
    class Meta:
        ordering = ('-creation',)

    name = models.CharField(max_length=100, verbose_name=_('name'))
    oembed = models.CharField(max_length=100, verbose_name=_('oembed'))

    creation = models.DateTimeField(editable=False, auto_now=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'attachments:detail', (), {'pk': self.pk}

    @property
    def metadata(self):
        try:
            return oembed.site.oembed(self.oembed).get_data()
        except:
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


class Attachment(MetaAttachment):
    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')


class File(MetaAttachment):
    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')

    type_choices = (
            ('link', _('link')),
            ('photo', _('photo')),
            ('video', _('video')),
            ('audio', _('audio')),
            ('rich', _('rich')),
            )

    file = models.FileField(upload_to='attachment_files', 
            verbose_name=_('file'))
    type = models.CharField(max_length=10, choices=type_choices, 
            verbose_name=_('type'))

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)
        if not self.oembed:
            self.oembed = self.get_oembed_url()
        return super(File, self).save(*args, **kwargs)

    def get_oembed_url(self):
        return 'http://{domain}{path}'.format(
                domain=Site.objects.get_current().domain,
                path=reverse('attachments:file', kwargs={'pk': self.pk}),
                )

    @property
    def oembed_type(self):
        return 'video' if self.type == 'audio' else unicode(self.type)
