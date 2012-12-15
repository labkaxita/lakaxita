from modeltranslation.translator import translator, TranslationOptions

from lakaxita.lost_found.models import Item, Notification


class ItemTO(TranslationOptions):
    fields = 'name', 'description'


class NotificationTO(TranslationOptions):
    fields = 'title', 'text'



registry = (
        (Item, ItemTO),
        (Notification, NotificationTO),
        )

for model, to in registry:
    translator.register(model, to)
