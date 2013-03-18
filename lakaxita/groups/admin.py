from django.contrib import admin
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import GroupAdmin

from imagekit.admin import AdminThumbnail
from grappelli_modeltranslation.admin import (TranslationAdmin, 
                                            TranslationStackedInline)

from lakaxita.groups.models import Group as LakaxitaGroup


class LakaxitaGroupAdmin(TranslationAdmin):
    search_fields = ('name', 'description')
    fields = ('name', 'image', 'description')


class LakaxitaGroupInline(TranslationStackedInline):
    model = LakaxitaGroup
    search_fields = ('name', 'description')
    list_display = ('name', 'admin_thumbnail')
    fields = ('name', 'image', 'description')

    admin_thumbnail = AdminThumbnail(image_field='thumbnail')


class GroupAdmin(GroupAdmin):
    inlines = [LakaxitaGroupInline]


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(LakaxitaGroup, LakaxitaGroupAdmin)
