from datetime import date
from django.contrib import admin
from django.core import urlresolvers
from django.utils.translation import ugettext as _

from markitup.widgets import AdminMarkItUpWidget
from imagekit.admin import AdminThumbnail
from grappelli_modeltranslation.admin import TranslationAdmin

from lakaxita.lost_found.models import Item, Notification


class NotificationInline(admin.TabularInline):
    model = Notification
    extra = 0
    fields = ('title', 'reply_to', 'date', 'text')
    readonly_fields = ('title', 'reply_to', 'date', 'text')

    def has_add_permission(self, request):
        return False


class ReturnedItemFilter(admin.SimpleListFilter):
    title = _('has been returned')
    parameter_name = 'returned'

    def lookups(self, request, model_admin):
        return (
                ('returned', _('Returned')),
                ('not_returned', _('Not returned')),
                )

    def queryset(self, request, queryset):
        if self.value() == 'returned':
            return queryset.filter(found__isnull=False)
        elif self.value() == 'not_returned':
            return queryset.filter(found__isnull=True)


class ItemAdmin(TranslationAdmin):
    search_fields = ('name', 'description')
    date_hierarchy = 'lost'
    fields = ('name', ('lost', 'found'), 'image', 'description')
    list_display = ('name', 'lost', 'found', 'has_been_returned', 
            'admin_thumbnail')
    list_filter = (ReturnedItemFilter,)
    inlines = [NotificationInline]
    actions = ['mark_returned', 'mark_not_returned']

    admin_thumbnail = AdminThumbnail(image_field='scaled_image')

    def has_been_returned(self, obj):
        return obj.has_been_returned
    has_been_returned.boolean = True
    has_been_returned.short_description = _('has been returned')

    def mark_returned(self, request, queryset):
        queryset.update(found=date.today())
    mark_returned.short_description = _('Mark as returned')

    def mark_not_returned(self, request, queryset):
        queryset.update(found=None)
    mark_not_returned.short_description = _('Mark as not returned')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(ItemAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('title', 'reply_to', 'text')
    date_hierarchy = 'date'
    fields = ('title', 'item', 'reply_to', 'date', 'text')
    readonly_fields = ('title', 'item', 'reply_to', 'date', 'text')
    list_display = ('title', 'item_link', 'reply_to', 'date')
    list_filter = ('date',)

    def has_add_permission(self, request):
        return False

    def item_link(self, obj):
        return '<a href="{link}">{item}</a>'.format(link=urlresolvers.reverse(
            'admin:lost_found_item_change', args=(obj.item.pk,)), item=obj.item)
    item_link.allow_tags = True
    item_link.short_description = _('item')

admin.site.register(Item, ItemAdmin)
admin.site.register(Notification, NotificationAdmin)
