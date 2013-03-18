from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _

from markitup.fields import MarkupField
from autoslug import AutoSlugField

from lakaxita.fields import ThumbnailField

class Group(models.Model):
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = MarkupField(max_length=500, blank=True, default='',
            verbose_name=_('description'))
    image = models.ImageField(blank=True, upload_to='groups', 
            verbose_name=_('image'))
    thumbnail = ThumbnailField(source='image')

    group = models.OneToOneField(Group, verbose_name=_('group'))
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name
