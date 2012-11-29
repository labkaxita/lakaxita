from datetime import date
from django.db import models
from django.utils.translation import ugettext as _

from markitup.fields import MarkupField
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField

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
        return self.filter(frontpage=True)

    def published(self):
        return self.filter(published__gte=date.today())

    def not_published(self):
        return self.filter(published__lt=date.today())
    

class News(models.Model):
    objects = QuerySetManager()
    queryset = QuerySet
    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news ')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = MarkupField(max_length=500, blank=True, 
            verbose_name=_('description'), 
            help_text=_('gotten from text if not defined'))
    text = MarkupField(verbose_name=_('text'))
    image = ImageField(blank=True, upload_to='news', verbose_name=_('image'))
    attachments = models.ManyToManyField(Attachment, blank=True, null=True,
            verbose_name=_('attachments'))

    published = models.DateField(default=date.today, verbose_name=_('publish on'))
    frontpage = models.BooleanField(default=True, verbose_name=_('on frontpage'))
    group = models.ForeignKey(Group, blank=True, null=True, 
            verbose_name=_('group it belongs to'))
    event = models.DateTimeField(blank=True, null=True, 
            verbose_name=_('event date'))

    slug = AutoSlugField(populate_from='title', unique=True)

    def __unicode__(self):
        return self.title

    @property
    def is_published(self):
        return self.published <= date.today()

    @models.permalink
    def get_absolute_url(self):
        return 'news:detail', (), {'slug': self.slug}
