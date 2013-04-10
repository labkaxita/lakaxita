from django.contrib import admin

from preferences.admin import PreferencesAdmin
from grappelli_modeltranslation.admin import TranslationAdmin

from lakaxita.preferences.models import SiteDescription


class SiteDescriptionAdmin(PreferencesAdmin, TranslationAdmin):
    pass

admin.site.register(SiteDescription, SiteDescriptionAdmin)
