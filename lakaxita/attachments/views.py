from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

from lakaxita.attachments.models import Attachment


class FileRedirect(RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        file_obj = get_object_or_404(Attachment, pk=self.kwargs['pk'])
        return file_obj.file.url
