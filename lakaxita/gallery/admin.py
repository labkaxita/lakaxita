from django.contrib import admin
from django.utils.translation import ugettext as _

from grappelli_modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin

#from lakaxita.attachments.admin import AttachmentInline, FileInline
from lakaxita.gallery.models import Category


class CategoryAdmin(TranslationAdmin, MPTTModelAdmin):
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
