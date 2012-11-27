from oembed.providers import DjangoProvider
import oembed

from lakaxita.attachments.models import File


class FileProvider(DjangoProvider):
    resource_type = 'rich'
    regex = r'(https?:\/\/(?:www[^\.]*\.)?localhost:8000)/attachments/file/(?P<pk>\d+)/$'

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

oembed.site.register(FileProvider)
