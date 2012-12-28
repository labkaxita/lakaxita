from modeltranslation.translator import translator, TranslationOptions

from lakaxita.lost_found.models import Item


class ItemTO(TranslationOptions):
    fields = 'name', 'description'


registry = (
        (Item, ItemTO),
        )

for model, to in registry:
    translator.register(model, to)
