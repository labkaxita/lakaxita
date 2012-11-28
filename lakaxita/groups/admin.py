from django.contrib import admin
from django.contrib.auth.models import Group as AuthGroup
from django.contrib.auth.admin import GroupAdmin

from sorl.thumbnail.admin import AdminImageMixin

from lakaxita.groups.models import Group


class GroupInline(admin.StackedInline):
    model = Group
    search_fields = ('name', 'description')
    fields = ('name', 'image', 'description')

class GroupAdmin(GroupAdmin):
    inlines = [GroupInline]

admin.site.unregister(AuthGroup)
admin.site.register(AuthGroup, GroupAdmin)
