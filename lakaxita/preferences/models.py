from django.db import models
from django.utils.translation import ugettext as _

from preferences.models import Preferences
from markitup.fields import MarkupField
from imagekit.models import ImageSpecField

from lakaxita.settings.images import scaled_options


class SiteDescription(Preferences):
    __module__ = 'preferences.models'

    class Meta:
        verbose_name = _('site description')
        verbose_name_plural = _('site description')

    image = models.ImageField(upload_to='preferences', 
                verbose_name=_('image'))
    scaled_image = ImageSpecField(source='image', **scaled_options)

    description = MarkupField(default='', verbose_name=_('description'))
