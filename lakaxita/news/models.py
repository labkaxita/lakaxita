from datetime import date
from django.db import models
from django.utils.translation import ugettext as _

from markitup.fields import MarkupField
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField

from lakaxita.settings.images import scaled_options, stretched_options
from lakaxita.groups.models import Group
from lakaxita.attachments.models import Attachment


class QuerySetManager(models.Manager):
    """A re-usable Manager to access a custom QuerySet"""
    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        return self.model.queryset(self.model)


class QuerySet(models.query.QuerySet):
    def frontpage(self):
        return self.published().filter(frontpage=True)

    def published(self):
        return self.filter(published__lte=date.today())

    def not_published(self):
        return self.filter(published__gt=date.today())
    

class News(models.Model):
    objects = QuerySetManager()
    queryset = QuerySet
    class Meta:
        ordering = ['-published', '-id']
        verbose_name = _('news')
        verbose_name_plural = _('news ')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    text = MarkupField(default='', verbose_name=_('text'))
    attachments = models.ManyToManyField(Attachment, blank=True, null=True,
            verbose_name=_('attachments'))

    published = models.DateField(default=date.today, verbose_name=_('publish on'))
    frontpage = models.BooleanField(default=True, verbose_name=_('on frontpage'))
    group = models.ForeignKey(Group, blank=True, null=True, 
            verbose_name=_('group it belongs to'))
    event = models.DateTimeField(blank=True, null=True, 
            verbose_name=_('event date'))

    image = models.ImageField(blank=True, upload_to='news', 
                    verbose_name=_('image'))
    scaled_image = ImageSpecField(source='image', **scaled_options)
    stretched_image = ImageSpecField(source='image', **stretched_options)

    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title

    @property
    def is_published(self):
        return self.published <= date.today()

    @models.permalink
    def get_absolute_url(self):
        return 'news:detail', (), {'slug': self.slug}
