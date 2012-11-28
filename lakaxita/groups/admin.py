from django.contrib import admin
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import GroupAdmin

from sorl.thumbnail.admin import AdminImageMixin

from lakaxita.groups.models import Group as LakaxitaGroup


class LakaxitaGroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    fields = ('name', 'image', 'description')

class LakaxitaGroupInline(admin.StackedInline):
    model = LakaxitaGroup
    search_fields = ('name', 'description')
    fields = ('name', 'image', 'description')

class GroupAdmin(GroupAdmin):
    inlines = [LakaxitaGroupInline]

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(LakaxitaGroup, LakaxitaGroupAdmin)
