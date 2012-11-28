from datetime import date
from django.contrib import admin
from django.utils.translation import ugettext as _

from sorl.thumbnail.admin import AdminImageMixin

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


class ItemAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ('name', 'description')
    date_hierarchy = 'lost'
    fields = ('name', ('lost', 'found'), 'image', 'description')
    list_display = ('name', 'lost', 'found', 'has_been_returned')
    list_filter = (ReturnedItemFilter,)
    inlines = [NotificationInline]
    actions = ['mark_returned', 'mark_not_returned']

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

admin.site.register(Item, ItemAdmin)
