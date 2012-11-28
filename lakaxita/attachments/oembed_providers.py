from oembed.providers import DjangoProvider
import oembed

from lakaxita.attachments.models import File


class FileProvider(DjangoProvider):
    provides = True
    resource_type = 'rich'

    class Meta:
        model = File
        named_view = 'attachments:file'
        fields_to_match = {'pk': 'pk'}
        resource_template_names = {
                'video': 'oembed/provider/video.yammy',
                'audio': 'oembed/provider/audio.yammy',
                'rich': 'oembed/provider/rich.yammy',
                }

    def title(self, obj):
        return obj.name

    def request_resource(self, url, **kwargs):
        obj = self.get_object(url)
        self.resource_type = obj.oembed_type
        self._meta.template_name = self._meta.resource_template_names.get(
                obj.type,
                self._meta.template_name,
                )
        return super(FileProvider, self).request_resource(url, **kwargs)

oembed.site.register(FileProvider)
