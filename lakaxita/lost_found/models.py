from datetime import date
from django.db import models
from django.utils.translation import ugettext as _

from autoslug import AutoSlugField
from markitup.fields import MarkupField
from imagekit.models import ProcessedImageField, ImageSpecField

from lakaxita.settings.images import scaled_options, stretched_options


class ItemManager(models.Manager):
    def not_returned(self):
        q = self.get_query_set()
        return q.filter(found__isnull=True)

    def returned(self):
        q = self.get_query_set()
        return q.filter(found__isnull=False)


class Item(models.Model):
    objects = ItemManager()
    class Meta:
        ordering = ['-lost']
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = MarkupField(blank=True, default='', 
            verbose_name=_('description'))

    lost = models.DateField(default=date.today, verbose_name=_('lost date'))
    found = models.DateField(blank=True, null=True, 
            verbose_name=_('found date'))

    image = models.ImageField(blank=True, upload_to='lost_found', 
            verbose_name=_('image'))
    scaled_image = ImageSpecField(source='image', **scaled_options)
    stretched_image = ImageSpecField(source='image', **stretched_options)

    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    @property
    def has_been_returned(self):
        return self.found is not None

    def get_absolute_url(self):
        return '/#/lost_found/{slug}/'.format(slug=self.slug)


class Notification(models.Model):
    class Meta:
        ordering = ['-date']
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    reply_to = models.EmailField(max_length=100, verbose_name=_('reply to'))
    text = models.TextField(blank=True, max_length=1000, 
            verbose_name=_('text'))

    date = models.DateField(default=date.today, verbose_name=('date'))
    item = models.ForeignKey(Item, verbose_name=_('item'))

    def __unicode__(self):
        return self.title
