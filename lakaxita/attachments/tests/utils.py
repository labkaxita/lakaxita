from django.contrib.sites.models import Site
import oembed
from lakaxita.attachments.oembed_providers import InternalAttachmentProvider


def fake_oembed_site():
    site = Site.objects.get_current()
    site.domain = 'localhost:8000'
    site.save()

    oembed.site = oembed.sites.ProviderSite()
    oembed.site.register(InternalAttachmentProvider)


