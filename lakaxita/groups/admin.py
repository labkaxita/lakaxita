from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from lakaxita.groups.models import Group


class GroupAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ('name', 'description')
    fields = (('name', 'group'), 'image', 'description')

admin.site.register(Group, GroupAdmin)
