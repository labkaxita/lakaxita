from django.db import models
from django.utils.translation import ugettext as _

from preferences.models import Preferences
from markitup.fields import MarkupField

from lakaxita.fields import ThumbnailField


class SiteDescription(Preferences):
    __module__ = 'preferences.models'

    class Meta:
        verbose_name = _('site description')
        verbose_name_plural = _('site description')

    image = models.ImageField(upload_to='preferences', 
            verbose_name=_('image'))
    thumbnail = ThumbnailField(source='image')

    description = MarkupField(default='', verbose_name=_('description'))
