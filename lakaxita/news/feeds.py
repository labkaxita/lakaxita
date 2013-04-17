from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _

from lakaxita.news.models import News


class NewsFeed(Feed):
    title = _('news from lakaxita')
    link = '/'
    description = _('latest news from lakaxita gaztetxea')

    def items(self):
        return News.objects.published()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item._text_rendered

    def item_link(self, item):
        return '/#/news/{slug}'.format(slug=item.slug)

    def item_categories(self, item):
        return [ attachment.oembed for attachment in item.attachments.all() ]
