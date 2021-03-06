from django.conf import settings

from oembed.providers import DjangoProvider
from oembed.utils import cleaned_sites
import oembed

from lakaxita.attachments.models import InternalAttachment


class InternalAttachmentProvider(DjangoProvider):
    provides = True
    resource_type = 'rich'

    class Meta:
        model = InternalAttachment
        named_view = 'attachments:file'
        fields_to_match = {'slug': 'slug'}
        resource_template_names = {
                'video': 'oembed/provider/video.yammy',
                'audio': 'oembed/provider/audio.yammy',
                'rich': 'oembed/provider/rich.yammy',
                }

    def title(self, obj):
        return obj.file.filename

    def author_name(self, obj):
        return settings.ATTACHMENTS['author_name']

    def author_url(self, obj):
        return settings.ATTACHMENTS['author_url']

    def request_resource(self, url, **kwargs):
        obj = self.get_object(url)
        self.resource_type = obj.oembed_type
        self._meta.template_name = self._meta.resource_template_names.get(
                obj.type,
                self._meta.template_name,
                )
        return super(InternalAttachmentProvider, self).request_resource(
                url, **kwargs)

oembed.site.register(InternalAttachmentProvider)
