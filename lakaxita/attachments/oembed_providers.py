from oembed.providers import DjangoProvider
from oembed import site

from lakaxita.attachments.models import File


class FileProvider(DjangoProvider):
    resource_type = 'rich'

    class Meta:
        model = File
        named_view = 'attachments:file'
        fields_to_match = {'pk': 'pk'}

    def title(self, obj):
        return obj.name

    def request_resource(self, url, **kwargs):
        obj = self.get_object(url)
        self.resource_type = obj.type
        return super(FileProvider, self).request_resource(url, **kwargs)

site.register(FileProvider)
