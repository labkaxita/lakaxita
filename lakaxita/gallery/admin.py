from django.contrib import admin
from django.utils.translation import ugettext as _

from grappelli_modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin

from lakaxita.gallery.models import Category


class CategoryAdmin(TranslationAdmin, MPTTModelAdmin):
    filter_horizontal = ('attachments',)
    search_fields = ('name', 'description')
    fieldsets = (
            (None, {
                'fields': (
                    ('name', 'parent'),
                    )}),
            (_('Media'), {
                'fields': (
                    ('attachments',),
                    )}),
            (_('Meta'), {
                'fields': (
                    ('description',),
                    )}),
                )
admin.site.register(Category, CategoryAdmin)
