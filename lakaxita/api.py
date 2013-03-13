from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.api import Api

from lakaxita.news.models import News
from lakaxita.attachments.models import Attachment
from lakaxita.groups.models import Group
from lakaxita.gallery.models import Category
from lakaxita.lost_found.models import Item


class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'lost_found'


class AttachmentResource(ModelResource):
    class Meta:
        queryset = Attachment.objects.all()
        resource_name = 'attachments'


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.root_nodes()
        resource_name = 'gallery'

    children = fields.ToManyField('self', 'children')
    parent = fields.ForeignKey('self', 'parent', null=True)
    attachments = fields.ToManyField(AttachmentResource, 'attachments')


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'groups'


class NewsResource(ModelResource):
    group = fields.ForeignKey(GroupResource, 'group', null=True)

    class Meta:
        queryset = News.objects.published()
        resource_name = 'news'

api = Api(api_name='api')
for resource in (ItemResource, CategoryResource, AttachmentResource,
                GroupResource, NewsResource):
    api.register(resource())
