from modeltranslation.translator import translator, TranslationOptions

from lakaxita.lost_found.models import Item
from lakaxita.news.models import News
from lakaxita.gallery.models import Category
from lakaxita.groups.models import Group


class ItemTO(TranslationOptions):
    fields = 'name', 'description'


class NewsTO(TranslationOptions):
    fields = 'title', 'text'


class CategoryTO(TranslationOptions):
    fields = 'name', 'description'


class GroupTO(TranslationOptions):
    fields = 'name', 'description'


registry = (
        (Item, ItemTO),
        (News, NewsTO),
        (Category, CategoryTO),
        (Group, GroupTO),
        )

for model, to in registry:
    translator.register(model, to)
