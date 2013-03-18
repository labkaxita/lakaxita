from django.contrib import admin
from django.utils.translation import ugettext as _

from imagekit.admin import AdminThumbnail
from grappelli_modeltranslation.admin import TranslationAdmin

from lakaxita.news.models import News
from lakaxita.groups.models import Group


class PublishedNewsFilter(admin.SimpleListFilter):
    title = _('has been published')
    parameter_name = 'has_been_published'

    def lookups(self, request, model_admin):
        return (
                ('published', _('Published')),
                ('not_published', _('Not published')),
                )

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.published()
        elif self.value() == 'not_published':
            return queryset.not_published()


class NewsAdmin(TranslationAdmin):
    search_fields = ('name',)
    date_hierarchy = 'published'
    list_display = ('title', 'frontpage', 'published', 'has_been_published', 
            'group', 'admin_thumbnail')
    list_filter = ('frontpage', 'published', PublishedNewsFilter, 'group')
    filter_horizontal = ('attachments',)
    fieldsets = (
            (None, {
                'fields': (
                    'title',
                    )}),
            (_('Meta'), {
                'fields': (
                    ('frontpage', 'published'), ('event', 'group'),
                    )}),
            (_('Media'), {
                'fields': (
                    'image', 'attachments'
                    )}),
            (None, {
                'fields': (
                    'text',
                    )}),
                )

    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

    def has_been_published(self, obj):
        return obj.is_published
    has_been_published.boolean = True
    has_been_published.short_description = _('has been published')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'group':
            if not request.user.is_superuser:
                kwargs['queryset'] = Group.objects.filter(
                        group__user=request.user)
        return super(NewsAdmin, self).formfield_for_foreignkey(
                db_field, request, **kwargs)

admin.site.register(News, NewsAdmin)
