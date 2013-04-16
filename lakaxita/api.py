from tastypie import fields
from tastypie.api import Api
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache

from lakaxita.news.models import News
from lakaxita.attachments.models import Attachment
from lakaxita.groups.models import Group
from lakaxita.gallery.models import Category
from lakaxita.lost_found.models import Item, Notification
from lakaxita.preferences.models import SiteDescription


class Resource(object):
    def dehydrate(self, bundle):
        for field in ['scaled_image', 'stretched_image']:
            value = getattr(bundle.obj, field, None)
            if hasattr(value, 'name') and value.name:
                bundle.data[field] = value.url
        return bundle


class ItemResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = Item.objects.all()
        resource_name = 'lost_items'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])
        fields = ['name', 'description', 'image', 'lost', 'found', 'slug']


class NotificationResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['post']
        authorization = Authorization()
        resource_name = 'lost_item_notifications'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])
        queryset = Notification.objects.all()
        fields = ['title', 'reply_to', 'text', 'item']

    item = fields.ForeignKey(ItemResource, 'item')


class AttachmentResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = Attachment.objects.all()
        resource_name = 'attachments'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])


class CategoryResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = Category.objects.root_nodes()
        resource_name = 'gallery'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])

    children = fields.ToManyField('self', 'children')
    parent = fields.ForeignKey('self', 'parent', null=True)
    attachments = fields.ToManyField(AttachmentResource, 'attachments')


class GroupResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = Group.objects.all()
        resource_name = 'groups'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])


class NewsResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = News.objects.published()
        resource_name = 'news'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])
        filtering = {'frontpage': ['exact']}
        fields = ['title', 'text', 'image', 'attachments', 'frontpage', 
                'group', 'event', 'slug', 'published']

    group = fields.ForeignKey(GroupResource, 'group', null=True)
    attachments = fields.ToManyField(AttachmentResource, 'attachments')


class SiteDescriptionResource(Resource, ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = SiteDescription.objects.all()
        resource_name = 'site_description'
        cache = SimpleCache(timeout=300, varies=["Accept", "Cookie"])
        fields = ['description', 'image']


api = Api(api_name='api')
for resource in (ItemResource, NotificationResource, CategoryResource, 
                AttachmentResource, GroupResource, NewsResource,
                SiteDescriptionResource):
    api.register(resource())
