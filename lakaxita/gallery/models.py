from django.db import models
from django.utils.translation import ugettext as _

from markitup.fields import MarkupField
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey

from lakaxita.attachments.models import Attachment


class Category(MPTTModel):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    name = models.CharField(max_length=50, verbose_name=_('name'))
    description = MarkupField(max_length=500, blank=True, 
            verbose_name=_('description'))
    attachments = models.ManyToManyField(Attachment, 
            verbose_name=_('attachments'))

    parent = TreeForeignKey('self', null=True, blank=True, 
            related_name='children', verbose_name=_('parent'))
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'gallery:detail', (), {'slug': self.slug}
