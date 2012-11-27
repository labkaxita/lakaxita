from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from oembed import site
from oembed.consumer import OEmbedConsumer


oembed_consumer = OEmbedConsumer()


class AttachmentManager(models.Manager):
    def for_model(self, model):
        """
        QuerySet for all attachments for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_query_set().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_unicode(model._get_pk_val()))
        return qs


class Attachment(models.Model):
    objects = AttachmentManager()
    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')

    oembed = models.CharField(max_length=100, verbose_name=_('oembed'))

    content_type = models.ForeignKey(ContentType)
    object_pk = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_pk')

    def __unicode__(self):
        return self.title if self.title else self.oembed

    @models.permalink
    def get_absolute_url(self):
        return 'attachments:detail', (), {'pk': self.pk}

    @property
    def metadata(self):
        try:
            return site.oembed(self.oembed).get_data()
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
                                                         

class File(models.Model):
    objects = AttachmentManager()
    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')

    type_choices = (
            ('photo', _('photo')),
            ('video', _('video')),
            ('rich', _('rich')),
            ('link', _('link')),
            )

    name = models.CharField(max_length=100, verbose_name=_('name'))
    file = models.FileField(upload_to='attachments', verbose_name=_('file'))
    type = models.CharField(max_length=10, choices=type_choices, 
            verbose_name=_('type'))

    content_type = models.ForeignKey(ContentType)
    object_pk = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_pk')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.file.url
